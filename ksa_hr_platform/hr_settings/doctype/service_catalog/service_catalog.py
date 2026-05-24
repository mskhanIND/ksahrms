import frappe
from frappe import _
from frappe.model.document import Document


class ServiceCatalog(Document):
    def validate(self):
        if not self.requires_line_manager and not self.requires_hr_manager and not self.requires_finance:
            frappe.throw(_("At least one approval layer is required."))

        if self.default_sla_hours is not None and self.default_sla_hours < 1:
            frappe.throw(_("Default SLA Hours must be at least 1."))
