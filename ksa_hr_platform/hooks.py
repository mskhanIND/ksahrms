app_name = "ksa_hr_platform"
app_title = "KSA HR Platform"
app_publisher = "KSA HR Platform Team"
app_description = "Process-oriented Saudi HR platform built under one owned namespace."
app_email = "support@example.com"
app_license = "MIT"

required_apps = ["frappe", "erpnext", "hrms"]

app_include_css = "/assets/ksa_hr_platform/css/ksa_hr_platform.css"
app_include_js = "/assets/ksa_hr_platform/js/ksa_hr_platform.js"

doc_events = {}
override_doctype_class = {}
override_whitelisted_methods = {}
fixtures = []

scheduler_events = {
    "daily": [
        "ksa_hr_platform.tasks.daily.process_due_hr_automations"
    ]
}
after_install = "ksa_hr_platform.setup.install.after_install"
after_migrate = "ksa_hr_platform.setup.migrate.after_migrate"
