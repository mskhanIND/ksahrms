import frappe
from frappe import _
from frappe.model.document import Document
from frappe.utils import add_days, cint, flt, now, today

from ksa_hr_platform.services.approval_engine import get_approval_plan
from ksa_hr_platform.services.notification_service import notify_service_request_event


class EmployeeServiceRequest(Document):
    def validate(self):
        self.apply_service_defaults()
        if self.docstatus == 0 and not self.process_status:
            self.process_status = "Draft"

    def before_submit(self):
        self.ensure_approval_plan()
        self.set_next_pending_approval()
        if not self.process_status or self.process_status == "Draft":
            self.process_status = "Submitted"

    def on_submit(self):
        self.set_next_pending_approval()
        notify_service_request_event(self, "submitted")

    def apply_service_defaults(self):
        if not self.service:
            return

        service = frappe.get_cached_doc("Service Catalog", self.service)
        if not self.priority:
            self.priority = service.default_priority or "Medium"
        if service.amount_required and not flt(self.amount):
            frappe.throw(_("Amount is required for service {0}.").format(service.service_name))

    def ensure_approval_plan(self):
        if self.approvals:
            return

        for row in get_approval_plan(self):
            self.append("approvals", row)

    def set_next_pending_approval(self):
        pending = self.get_next_pending_approval()
        if pending:
            self.process_status = pending.approval_stage
            self.pending_approval_stage = pending.approval_stage
            self.pending_approval_role = pending.approver_role
            self.pending_approval_user = pending.approver_user
            return

        self.pending_approval_stage = None
        self.pending_approval_role = None
        self.pending_approval_user = None
        if self.process_status not in ("Completed", "Rejected", "Cancelled"):
            self.process_status = "Fulfilment"
            self.ensure_fulfilment_task()

    def get_next_pending_approval(self):
        rows = sorted(self.approvals, key=lambda row: cint(row.sequence or 0))
        for row in rows:
            if row.status == "Pending":
                return row
        return None

    def ensure_fulfilment_task(self):
        if self.fulfilment_tasks:
            return

        settings = frappe.get_single("HR Platform Settings")
        if not cint(settings.auto_create_fulfilment_task):
            return

        service = frappe.get_cached_doc("Service Catalog", self.service)
        sla_hours = cint(service.default_sla_hours or settings.default_service_sla_hours or 48)
        due_date = self.required_by or add_days(today(), max(1, int((sla_hours + 23) / 24)))
        self.append(
            "fulfilment_tasks",
            {
                "task_subject": _("Fulfil {0}").format(service.service_name),
                "owner_role": service.fulfilment_role or "HR User",
                "due_date": due_date,
                "task_status": "Open",
            },
        )

    def approve_current_step(self, comments=None):
        self.flags.ignore_validate_update_after_submit = True
        row = self.get_next_pending_approval()
        if not row:
            frappe.throw(_("There is no pending approval step."))

        self.validate_current_user_can_approve(row)
        row.status = "Approved"
        row.action_by = frappe.session.user
        row.action_on = now()
        row.comments = comments
        self.set_next_pending_approval()
        notify_service_request_event(self, "approved")

    def reject_request(self, comments=None):
        self.flags.ignore_validate_update_after_submit = True
        row = self.get_next_pending_approval()
        if row:
            self.validate_current_user_can_approve(row)
            row.status = "Rejected"
            row.action_by = frappe.session.user
            row.action_on = now()
            row.comments = comments
        self.process_status = "Rejected"
        self.pending_approval_stage = None
        self.pending_approval_role = None
        self.pending_approval_user = None
        notify_service_request_event(self, "rejected")

    def mark_completed(self, comments=None):
        self.flags.ignore_validate_update_after_submit = True
        if self.get_next_pending_approval():
            frappe.throw(_("All approval steps must be approved before completion."))

        for task in self.fulfilment_tasks:
            if task.task_status != "Cancelled":
                task.task_status = "Completed"
                task.completed_on = task.completed_on or now()
                if comments:
                    task.notes = comments

        self.process_status = "Completed"
        self.completed_on = now()
        notify_service_request_event(self, "completed")

    def validate_current_user_can_approve(self, approval_row):
        if "System Manager" in frappe.get_roles():
            return

        if approval_row.approver_user and approval_row.approver_user != frappe.session.user:
            frappe.throw(_("Only {0} can approve this step.").format(approval_row.approver_user))

        if approval_row.approver_role and approval_row.approver_role not in frappe.get_roles():
            frappe.throw(_("Role {0} is required to approve this step.").format(approval_row.approver_role))
