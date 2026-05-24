from frappe import _


def get_data():
    return [
        {"module_name": "Workforce Core", "type": "module", "label": _("Workforce Core"), "color": "blue", "icon": "octicon octicon-organization"},
        {"module_name": "Recruitment Onboarding", "type": "module", "label": _("Recruitment Onboarding"), "color": "green", "icon": "octicon octicon-person-add"},
        {"module_name": "Attendance Time", "type": "module", "label": _("Attendance Time"), "color": "orange", "icon": "octicon octicon-clock"},
        {"module_name": "Leave Benefits", "type": "module", "label": _("Leave Benefits"), "color": "cyan", "icon": "octicon octicon-calendar"},
        {"module_name": "Payroll Compensation", "type": "module", "label": _("Payroll Compensation"), "color": "purple", "icon": "octicon octicon-credit-card"},
        {"module_name": "Employee Services", "type": "module", "label": _("Employee Services"), "color": "yellow", "icon": "octicon octicon-inbox"},
        {"module_name": "Offboarding Settlement", "type": "module", "label": _("Offboarding Settlement"), "color": "red", "icon": "octicon octicon-sign-out"},
        {"module_name": "Accruals Finance", "type": "module", "label": _("Accruals Finance"), "color": "gray", "icon": "octicon octicon-book"},
        {"module_name": "Analytics Compliance", "type": "module", "label": _("Analytics Compliance"), "color": "blue", "icon": "octicon octicon-graph"},
        {"module_name": "HR Settings", "type": "module", "label": _("HR Settings"), "color": "darkgrey", "icon": "octicon octicon-gear"},
    ]
