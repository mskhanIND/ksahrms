from __future__ import annotations

import frappe
from frappe.utils import cint, get_link_to_form


EVENT_SUBJECTS = {
    "submitted": "Employee Service Request submitted",
    "approved": "Employee Service Request approval updated",
    "rejected": "Employee Service Request rejected",
    "completed": "Employee Service Request completed",
}


def notify_service_request_event(doc, event: str) -> None:
    if not notifications_enabled():
        return

    recipients = get_recipients(doc, event)
    if not recipients:
        return

    subject = f"{EVENT_SUBJECTS.get(event, 'Employee Service Request update')}: {doc.name}"
    message = build_message(doc, event)
    frappe.sendmail(recipients=recipients, subject=subject, message=message, delayed=True)


def notifications_enabled() -> bool:
    if not frappe.db.exists("DocType", "HR Platform Settings"):
        return False
    settings = frappe.get_single("HR Platform Settings")
    return cint(settings.enable_email_notifications)


def get_recipients(doc, event: str) -> list[str]:
    recipients: set[str] = set()

    if event in ("submitted", "approved") and doc.pending_approval_user:
        recipients.add(doc.pending_approval_user)

    if event in ("submitted", "approved") and doc.pending_approval_role:
        recipients.update(get_users_with_role(doc.pending_approval_role))

    if event in ("rejected", "completed") and doc.owner:
        recipients.add(doc.owner)

    return sorted(user for user in recipients if user and user != "Administrator")


def get_users_with_role(role: str) -> list[str]:
    return frappe.get_all(
        "Has Role",
        filters={"role": role, "parenttype": "User"},
        pluck="parent",
    )


def build_message(doc, event: str) -> str:
    link = get_link_to_form(doc.doctype, doc.name)
    return f"""
    <p>Request: {link}</p>
    <p>Status: {doc.process_status}</p>
    <p>Service: {doc.service_name or doc.service}</p>
    <p>Subject: {doc.subject}</p>
    """
