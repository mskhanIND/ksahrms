import frappe


PLATFORM_ROLES = [
    "Employee Self Service",
    "Line Manager",
    "HR User",
    "HR Manager",
    "Payroll User",
    "Payroll Manager",
    "Finance User",
    "Finance Manager",
    "Compliance Officer",
]

DEFAULT_SERVICES = [
    {
        "service_code": "HR-LETTER",
        "service_name": "HR Letter Request",
        "service_category": "Letter",
        "requires_line_manager": 0,
        "requires_hr_manager": 1,
        "requires_finance": 0,
        "fulfilment_role": "HR User",
    },
    {
        "service_code": "TRAVEL",
        "service_name": "Travel Request",
        "service_category": "Travel",
        "requires_line_manager": 1,
        "requires_hr_manager": 1,
        "requires_finance": 1,
        "fulfilment_role": "HR User",
    },
    {
        "service_code": "ASSET",
        "service_name": "Asset Request",
        "service_category": "Asset",
        "requires_line_manager": 1,
        "requires_hr_manager": 1,
        "requires_finance": 0,
        "fulfilment_role": "HR User",
    },
    {
        "service_code": "INSURANCE",
        "service_name": "Insurance Service Request",
        "service_category": "Insurance",
        "requires_line_manager": 0,
        "requires_hr_manager": 1,
        "requires_finance": 0,
        "fulfilment_role": "HR User",
    },
    {
        "service_code": "PAYMENT",
        "service_name": "Payment Request",
        "service_category": "Payment",
        "requires_line_manager": 1,
        "requires_hr_manager": 1,
        "requires_finance": 1,
        "fulfilment_role": "Finance User",
        "amount_required": 1,
    },
]


def after_install():
    create_roles()
    create_default_settings()
    create_default_services()


def create_roles():
    for role_name in PLATFORM_ROLES:
        if frappe.db.exists("Role", role_name):
            continue
        frappe.get_doc(
            {
                "doctype": "Role",
                "role_name": role_name,
                "desk_access": 1,
            }
        ).insert(ignore_permissions=True)


def create_default_settings():
    settings = frappe.get_single("HR Platform Settings")
    settings.employee_service_request_series = settings.employee_service_request_series or "ESR-.YYYY.-.#####"
    settings.default_service_sla_hours = settings.default_service_sla_hours or 48
    settings.reminder_before_sla_hours = settings.reminder_before_sla_hours or 4
    settings.auto_create_fulfilment_task = 1
    settings.enable_email_notifications = 1
    settings.save(ignore_permissions=True)


def create_default_services():
    for service in DEFAULT_SERVICES:
        if frappe.db.exists("Service Catalog", service["service_code"]):
            continue
        doc = frappe.get_doc({"doctype": "Service Catalog", "active": 1, "default_sla_hours": 48, "default_priority": "Medium", **service})
        doc.insert(ignore_permissions=True)
