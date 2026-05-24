import frappe
from frappe import _
from frappe.model.document import Document


class ApprovalMatrix(Document):
    def validate(self):
        if self.min_amount and self.max_amount and self.min_amount > self.max_amount:
            frappe.throw(_("Minimum Amount cannot be greater than Maximum Amount."))

        sequences = [row.sequence for row in self.approval_steps if row.required]
        if sequences and len(sequences) != len(set(sequences)):
            frappe.throw(_("Approval step sequence numbers must be unique."))
