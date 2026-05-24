import frappe


@frappe.whitelist()
def approve_request(name: str, comments: str | None = None):
    doc = frappe.get_doc("Employee Service Request", name)
    doc.approve_current_step(comments)
    doc.save()
    return doc.as_dict()


@frappe.whitelist()
def reject_request(name: str, comments: str | None = None):
    doc = frappe.get_doc("Employee Service Request", name)
    doc.reject_request(comments)
    doc.save()
    return doc.as_dict()


@frappe.whitelist()
def complete_request(name: str, comments: str | None = None):
    doc = frappe.get_doc("Employee Service Request", name)
    doc.mark_completed(comments)
    doc.save()
    return doc.as_dict()
