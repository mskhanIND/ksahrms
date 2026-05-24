from frappe.model.document import Document


class EmployeeHRProfile(Document):
    def validate(self):
        if not self.process_status:
            self.process_status = "Draft"

        if not self.title:
            self.title = self.name
