import json

import frappe


PROCESS_GUIDES = [
    {
        "sequence": 1,
        "process_name": "Start Here",
        "module": "HR Settings",
        "status": "Available",
        "owner_role": "HR Manager",
        "start_point": "Open HR Platform Settings, review default services, then create or adjust approval rules.",
        "end_point": "A working service request can be submitted, approved, fulfilled, and completed.",
        "workflow_summary": "Settings -> Service Catalog -> Approval Matrix -> Employee Service Request -> Fulfilment.",
        "approval_strategy": "Service Catalog provides a default approval path. Approval Matrix overrides it for specific company, department, service, or amount rules.",
        "notification_strategy": "Submitted, approved, rejected, and completed request events call the email notification service when email notifications are enabled.",
        "next_action": "Go to HR Platform Settings, then review Service Catalog records.",
        "related_doctypes": [
            [
                "HR Platform Settings",
                "Setup"
            ],
            [
                "Service Catalog",
                "Setup"
            ],
            [
                "Approval Matrix",
                "Setup"
            ],
            [
                "Employee Service Request",
                "Transaction"
            ]
        ]
    },
    {
        "sequence": 2,
        "process_name": "Request To Approval",
        "module": "Employee Services",
        "status": "Available",
        "owner_role": "HR User",
        "start_point": "Employee or HR creates an Employee Service Request from the selected Service Catalog item.",
        "end_point": "Request is completed after all approval rows are approved and fulfilment tasks are closed.",
        "workflow_summary": "Draft -> Submitted -> Line Manager Review -> HR Review -> Finance Review -> Fulfilment -> Completed.",
        "approval_strategy": "The request creates ordered approval rows from Approval Matrix or from Service Catalog defaults.",
        "notification_strategy": "Pending approvers are notified on submit and approval progress. Request owner is notified on rejection and completion.",
        "next_action": "Create an Employee Service Request and submit it.",
        "related_doctypes": [
            [
                "Employee Service Request",
                "Transaction"
            ],
            [
                "Employee Service Request Approval",
                "Child Table"
            ],
            [
                "Service Fulfilment Task",
                "Child Table"
            ]
        ]
    },
    {
        "sequence": 3,
        "process_name": "Workforce Foundation",
        "module": "Workforce Core",
        "status": "Foundation",
        "owner_role": "HR Manager",
        "start_point": "Create or review Employee HR Profile records linked to ERPNext Employee.",
        "end_point": "Saudi-specific HR profile, documents, dependents, contracts, and employment data are controlled from one profile.",
        "workflow_summary": "Employee -> Employee HR Profile -> Profile Review -> Active Profile.",
        "approval_strategy": "HR validates profile completeness. HR Manager approves sensitive corrections.",
        "notification_strategy": "Profile missing data, document expiry, and HR review reminders are planned.",
        "next_action": "Open Employee HR Profile and validate employee master coverage.",
        "related_doctypes": [
            [
                "Employee HR Profile",
                "Foundation"
            ]
        ]
    },
    {
        "sequence": 4,
        "process_name": "Hire To Join",
        "module": "Recruitment Onboarding",
        "status": "Foundation",
        "owner_role": "HR Manager",
        "start_point": "Department raises hiring need or replacement request.",
        "end_point": "Employee record is active, joining checklist is complete, and probation review is scheduled.",
        "workflow_summary": "Workforce Plan -> Hiring Request -> Candidate -> Offer -> Joining -> Probation.",
        "approval_strategy": "Department Head, HR, Finance where budget applies, and authorized offer approver.",
        "notification_strategy": "Hiring approval, interview scheduling, offer approval, joining checklist, and probation reminders.",
        "next_action": "Open Hiring Request and define the first hire-to-join process.",
        "related_doctypes": [
            [
                "Hiring Request",
                "Foundation"
            ]
        ]
    },
    {
        "sequence": 5,
        "process_name": "Time To Pay",
        "module": "Attendance Time",
        "status": "Foundation",
        "owner_role": "Payroll Manager",
        "start_point": "Attendance, leave, shift, overtime, or exception data enters the month.",
        "end_point": "Payroll-impacting adjustments are approved and included in payroll run controls.",
        "workflow_summary": "Device Sync -> Attendance Exception -> Approval -> Payroll Adjustment -> Payroll Run.",
        "approval_strategy": "Line Manager validates exceptions, HR validates policy, Payroll validates salary impact.",
        "notification_strategy": "Device sync failures, pending overtime/exception approvals, and payroll readiness alerts.",
        "next_action": "Open Attendance Exception and model the first attendance correction workflow.",
        "related_doctypes": [
            [
                "Attendance Exception",
                "Foundation"
            ]
        ]
    },
    {
        "sequence": 6,
        "process_name": "Leave And Benefits",
        "module": "Leave Benefits",
        "status": "Foundation",
        "owner_role": "HR Manager",
        "start_point": "Employee or HR records a leave/benefit entitlement, request, due, or exception.",
        "end_point": "Leave/benefit decision is approved and reflected in employee service or payroll process.",
        "workflow_summary": "Leave Benefit Request -> HR Review -> Manager/Payroll Review -> Approved -> Closed.",
        "approval_strategy": "HR validates entitlement. Manager or Payroll approves impact depending on request type.",
        "notification_strategy": "Pending entitlement review, approval decisions, and overdue benefit tasks are planned.",
        "next_action": "Open Leave Benefit Request and define the first leave/benefit service type.",
        "related_doctypes": [
            [
                "Leave Benefit Request",
                "Foundation"
            ]
        ]
    },
    {
        "sequence": 7,
        "process_name": "Payroll Compensation",
        "module": "Payroll Compensation",
        "status": "Foundation",
        "owner_role": "Payroll Manager",
        "start_point": "Payroll receives an approved salary, benefit, overtime, deduction, or correction impact.",
        "end_point": "Payroll adjustment is approved and ready for Salary Slip or Payroll Entry processing.",
        "workflow_summary": "Payroll Adjustment -> Payroll Review -> Finance Review -> Approved For Payroll.",
        "approval_strategy": "Payroll validates salary impact. Finance validates accounting impact for payable items.",
        "notification_strategy": "Payroll review, finance review, approval, rejection, and payroll-ready alerts are planned.",
        "next_action": "Open Payroll Adjustment and map first salary-impact transaction.",
        "related_doctypes": [
            [
                "Payroll Adjustment",
                "Foundation"
            ]
        ]
    },
    {
        "sequence": 8,
        "process_name": "Exit To Settlement",
        "module": "Offboarding Settlement",
        "status": "Foundation",
        "owner_role": "HR Manager",
        "start_point": "Resignation, termination, final exit, or contract-end action is initiated.",
        "end_point": "Clearance is complete, final settlement is approved, and payment/accounting records are posted.",
        "workflow_summary": "Exit Case -> Clearance -> EOS Calculation -> Payroll Review -> Finance Review -> Settled.",
        "approval_strategy": "HR validates policy, departments confirm clearance, Payroll validates dues, Finance validates payment.",
        "notification_strategy": "Clearance assignment, overdue clearance, settlement approval, and completion notices.",
        "next_action": "Open Exit Case and define the first exit-to-settlement flow.",
        "related_doctypes": [
            [
                "Exit Case",
                "Foundation"
            ]
        ]
    },
    {
        "sequence": 9,
        "process_name": "Accrual To Journal",
        "module": "Accruals Finance",
        "status": "Foundation",
        "owner_role": "Finance Manager",
        "start_point": "Monthly accrual schedule becomes due.",
        "end_point": "Journal proposal is reviewed, posted, and reconciled.",
        "workflow_summary": "Accrual Policy -> Calculation Batch -> Journal Proposal -> Posted -> Reconciled.",
        "approval_strategy": "HR validates employee assumptions. Finance validates accounts, cost centers, and journals.",
        "notification_strategy": "Schedule due, calculation completed, journal posting failed, and reconciliation pending.",
        "next_action": "Open Accrual Policy and define the first monthly accrual rule.",
        "related_doctypes": [
            [
                "Accrual Policy",
                "Foundation"
            ]
        ]
    },
    {
        "sequence": 10,
        "process_name": "Compliance To Action",
        "module": "Analytics Compliance",
        "status": "Foundation",
        "owner_role": "Compliance Officer",
        "start_point": "A document expiry, policy exception, dashboard condition, or compliance risk is detected.",
        "end_point": "Compliance action is assigned, resolved, and closed by HR or the responsible owner.",
        "workflow_summary": "Compliance Alert -> Assigned -> In Progress -> Resolved -> Closed.",
        "approval_strategy": "Compliance Officer or HR Manager closes high-risk alerts after owner resolution.",
        "notification_strategy": "Upcoming expiry, breach, assigned action, overdue action, and closure notifications are planned.",
        "next_action": "Open Compliance Alert and define the first document expiry alert.",
        "related_doctypes": [
            [
                "Compliance Alert",
                "Foundation"
            ]
        ]
    }
]

LEGACY_WORKSPACES = [
    {
        "label": "KSA HR Platform",
        "title": "KSA HR Platform",
        "module": "HR Settings",
        "sequence_id": 1,
        "headline": "Start here: configure HR Settings, then run Employee Service Requests.",
        "description": "This workspace shows available process DocTypes, foundation process owners, and the planned end-to-end HR map.",
        "links": [
            [
                "HR Process Guide",
                "Start Here"
            ],
            [
                "HR Platform Settings",
                "1. HR Platform Settings"
            ],
            [
                "Service Catalog",
                "2. Service Catalog"
            ],
            [
                "Approval Matrix",
                "3. Approval Matrix"
            ],
            [
                "Employee Service Request",
                "4. Employee Service Request"
            ],
            [
                "Employee HR Profile",
                "Employee HR Profile"
            ],
            [
                "Hiring Request",
                "Hiring Request"
            ],
            [
                "Attendance Exception",
                "Attendance Exception"
            ],
            [
                "Leave Benefit Request",
                "Leave Benefit Request"
            ],
            [
                "Payroll Adjustment",
                "Payroll Adjustment"
            ],
            [
                "Exit Case",
                "Exit Case"
            ],
            [
                "Accrual Policy",
                "Accrual Policy"
            ],
            [
                "Compliance Alert",
                "Compliance Alert"
            ]
        ]
    },
    {
        "label": "KSA HR Settings",
        "title": "KSA HR Settings",
        "module": "HR Settings",
        "sequence_id": 2,
        "headline": "Control center for policies, services, approvals, and user guidance.",
        "description": "Begin here before running transactions. These DocTypes decide how requests move and who approves.",
        "links": [
            [
                "HR Platform Settings",
                "HR Platform Settings"
            ],
            [
                "Service Catalog",
                "Service Catalog"
            ],
            [
                "Approval Matrix",
                "Approval Matrix"
            ],
            [
                "HR Process Guide",
                "HR Process Guide"
            ]
        ]
    },
    {
        "label": "KSA Employee Services",
        "title": "KSA Employee Services",
        "module": "Employee Services",
        "sequence_id": 3,
        "headline": "First operational slice: request, approve, fulfil, complete.",
        "description": "Create service requests here. Approval rows and fulfilment tasks are created inside the request.",
        "links": [
            [
                "Employee Service Request",
                "Employee Service Request"
            ],
            [
                "Service Catalog",
                "Service Catalog"
            ],
            [
                "Approval Matrix",
                "Approval Matrix"
            ],
            [
                "HR Process Guide",
                "Request To Approval Guide"
            ]
        ]
    },
    {
        "label": "KSA Workforce Core",
        "title": "KSA Workforce Core",
        "module": "Workforce Core",
        "sequence_id": 4,
        "headline": "Single owned profile for Saudi-specific HR data linked to the standard Employee record.",
        "description": "Start: Create or sync an employee profile from ERPNext Employee. End: Employee profile is complete, reviewed, and ready for downstream HR processes.",
        "links": [
            [
                "Employee HR Profile",
                "Employee HR Profile"
            ],
            [
                "HR Process Guide",
                "Workforce Core Guide"
            ],
            [
                "Employee Service Request",
                "Employee Service Request"
            ]
        ]
    },
    {
        "label": "KSA Recruitment Onboarding",
        "title": "KSA Recruitment Onboarding",
        "module": "Recruitment Onboarding",
        "sequence_id": 5,
        "headline": "Controlled starting point for recruitment, replacement, and workforce demand.",
        "description": "Start: Department requests a new position or replacement. End: Hiring request is approved and ready for candidate processing.",
        "links": [
            [
                "Hiring Request",
                "Hiring Request"
            ],
            [
                "HR Process Guide",
                "Recruitment Onboarding Guide"
            ],
            [
                "Employee Service Request",
                "Employee Service Request"
            ]
        ]
    },
    {
        "label": "KSA Attendance Time",
        "title": "KSA Attendance Time",
        "module": "Attendance Time",
        "sequence_id": 6,
        "headline": "Controlled correction path for attendance, shift, overtime, late, early, and device exceptions.",
        "description": "Start: Employee, manager, HR, or device sync identifies an attendance exception. End: Approved correction is ready for attendance or payroll impact.",
        "links": [
            [
                "Attendance Exception",
                "Attendance Exception"
            ],
            [
                "HR Process Guide",
                "Attendance Time Guide"
            ],
            [
                "Employee Service Request",
                "Employee Service Request"
            ]
        ]
    },
    {
        "label": "KSA Leave Benefits",
        "title": "KSA Leave Benefits",
        "module": "Leave Benefits",
        "sequence_id": 7,
        "headline": "Unified control point for leave dues, tickets, benefits, encashment, and benefit exceptions.",
        "description": "Start: Employee or HR requests a leave or benefit action. End: Benefit decision is approved and handed to service, payroll, or compliance process.",
        "links": [
            [
                "Leave Benefit Request",
                "Leave Benefit Request"
            ],
            [
                "HR Process Guide",
                "Leave Benefits Guide"
            ],
            [
                "Employee Service Request",
                "Employee Service Request"
            ]
        ]
    },
    {
        "label": "KSA Payroll Compensation",
        "title": "KSA Payroll Compensation",
        "module": "Payroll Compensation",
        "sequence_id": 8,
        "headline": "Controlled payroll-impact record for approved salary, benefit, overtime, and deduction changes.",
        "description": "Start: Approved HR process creates or requests a payroll-impacting adjustment. End: Adjustment is approved for salary slip or payroll entry processing.",
        "links": [
            [
                "Payroll Adjustment",
                "Payroll Adjustment"
            ],
            [
                "HR Process Guide",
                "Payroll Compensation Guide"
            ],
            [
                "Employee Service Request",
                "Employee Service Request"
            ]
        ]
    },
    {
        "label": "KSA Offboarding Settlement",
        "title": "KSA Offboarding Settlement",
        "module": "Offboarding Settlement",
        "sequence_id": 9,
        "headline": "Controlled start-to-finish record for resignation, termination, clearance, and settlement.",
        "description": "Start: Exit is initiated by employee, manager, HR, or contract end. End: Clearance, EOS calculation, final approval, and settlement are complete.",
        "links": [
            [
                "Exit Case",
                "Exit Case"
            ],
            [
                "HR Process Guide",
                "Offboarding Settlement Guide"
            ],
            [
                "Employee Service Request",
                "Employee Service Request"
            ]
        ]
    },
    {
        "label": "KSA Accruals Finance",
        "title": "KSA Accruals Finance",
        "module": "Accruals Finance",
        "sequence_id": 10,
        "headline": "Policy and control record for monthly HR accrual calculations and finance provisions.",
        "description": "Start: Finance defines a recurring HR accrual rule. End: Policy drives reviewed accrual calculation and journal proposal.",
        "links": [
            [
                "Accrual Policy",
                "Accrual Policy"
            ],
            [
                "HR Process Guide",
                "Accruals Finance Guide"
            ],
            [
                "Employee Service Request",
                "Employee Service Request"
            ]
        ]
    },
    {
        "label": "KSA Analytics Compliance",
        "title": "KSA Analytics Compliance",
        "module": "Analytics Compliance",
        "sequence_id": 11,
        "headline": "Actionable alert for document expiry, policy exception, dashboard trigger, or HR compliance risk.",
        "description": "Start: A compliance rule, report, or user identifies a risk. End: Responsible owner resolves the action and HR/Compliance closes it.",
        "links": [
            [
                "Compliance Alert",
                "Compliance Alert"
            ],
            [
                "HR Process Guide",
                "Analytics Compliance Guide"
            ],
            [
                "Employee Service Request",
                "Employee Service Request"
            ]
        ]
    }
]

WORKSPACE_SECTIONS = [
    {
        "title": "Start Here",
        "description": "Configure the platform first, then run the employee service request flow from request to approval to fulfilment.",
        "items": [
            ("HR Process Guide", "Process Guide"),
            ("HR Platform Settings", "1. HR Platform Settings"),
            ("Service Catalog", "2. Service Catalog"),
            ("Approval Matrix", "3. Approval Matrix"),
            ("Employee Service Request", "4. Employee Service Request"),
        ],
    },
    {
        "title": "Workforce Core",
        "description": "Employee master control for Saudi-specific HR profile data before downstream HR activity starts.",
        "items": [("Employee HR Profile", "Employee HR Profile")],
    },
    {
        "title": "Recruitment Onboarding",
        "description": "Hire-to-join process ownership from hiring need to approved recruitment action.",
        "items": [("Hiring Request", "Hiring Request")],
    },
    {
        "title": "Attendance Time",
        "description": "Time-to-pay controls for attendance, overtime, shift, late, early, and device-sync exceptions.",
        "items": [("Attendance Exception", "Attendance Exception")],
    },
    {
        "title": "Leave Benefits",
        "description": "Leave, ticket, benefit, encashment, and benefit exception requests controlled in one path.",
        "items": [("Leave Benefit Request", "Leave Benefit Request")],
    },
    {
        "title": "Payroll Compensation",
        "description": "Payroll-impacting salary, benefit, overtime, deduction, and correction adjustments.",
        "items": [("Payroll Adjustment", "Payroll Adjustment")],
    },
    {
        "title": "Offboarding Settlement",
        "description": "Exit-to-settlement ownership for resignation, clearance, EOS calculation, and final settlement.",
        "items": [("Exit Case", "Exit Case")],
    },
    {
        "title": "Accruals Finance",
        "description": "Monthly HR accrual policy ownership before calculation, journal proposal, and reconciliation.",
        "items": [("Accrual Policy", "Accrual Policy")],
    },
    {
        "title": "Analytics Compliance",
        "description": "Compliance-to-action ownership for document expiry, policy exception, and HR compliance risk alerts.",
        "items": [("Compliance Alert", "Compliance Alert")],
    },
]

LEGACY_WORKSPACE_LABELS = [
    workspace["label"]
    for workspace in LEGACY_WORKSPACES
    if workspace["label"] != "KSA HR Platform"
]

WORKSPACES = [
    {
        "label": "KSA HR Platform",
        "title": "KSA HR Platform",
        "module": "HR Settings",
        "sequence_id": 1,
        "headline": "Start here: configure HR Settings, then run Employee Service Requests.",
        "description": "All KSA HR process areas are grouped here so the Desk stays clean and every process shows its mapped DocTypes.",
        "sections": WORKSPACE_SECTIONS,
    }
]

def create_onboarding_records():
    create_process_guides()
    create_workspaces()


def create_process_guides():
    if not frappe.db.exists("DocType", "HR Process Guide"):
        return

    for guide in PROCESS_GUIDES:
        if frappe.db.exists("HR Process Guide", guide["process_name"]):
            doc = frappe.get_doc("HR Process Guide", guide["process_name"])
        else:
            doc = frappe.new_doc("HR Process Guide")
            doc.process_name = guide["process_name"]

        doc.sequence = guide["sequence"]
        doc.module_name = guide["module"]
        doc.status = guide["status"]
        doc.owner_role = guide["owner_role"]
        doc.start_point = guide["start_point"]
        doc.end_point = guide["end_point"]
        doc.workflow_summary = guide["workflow_summary"]
        doc.approval_strategy = guide["approval_strategy"]
        doc.notification_strategy = guide["notification_strategy"]
        doc.next_action = guide["next_action"]
        doc.set("related_doctypes", [])

        for doctype_name, purpose in guide["related_doctypes"]:
            doc.append(
                "related_doctypes",
                {
                    "doctype_name": doctype_name,
                    "purpose": purpose,
                    "current_status": "Available",
                },
            )

        doc.save(ignore_permissions=True)


def create_workspaces():
    if not frappe.db.exists("DocType", "Workspace"):
        return

    hide_legacy_workspaces()

    for workspace in WORKSPACES:
        if frappe.db.exists("Workspace", workspace["label"]):
            doc = frappe.get_doc("Workspace", workspace["label"])
        else:
            doc = frappe.new_doc("Workspace")
            doc.name = workspace["label"]

        safe_set(doc, "label", workspace["label"])
        safe_set(doc, "title", workspace["title"])
        safe_set(doc, "module", workspace["module"])
        safe_set(doc, "public", 1)
        safe_set(doc, "is_hidden", 0)
        safe_set(doc, "parent_page", "")
        safe_set(doc, "sequence_id", workspace["sequence_id"])
        safe_set(doc, "indicator_color", "green")
        safe_set(doc, "icon", "organization")

        if doc.meta.has_field("content"):
            doc.content = json.dumps(build_workspace_content(workspace))

        set_workspace_child_rows(doc, "links", build_workspace_links(workspace))
        set_workspace_child_rows(doc, "shortcuts", build_workspace_shortcuts(workspace))

        doc.save(ignore_permissions=True)


def hide_legacy_workspaces():
    for label in LEGACY_WORKSPACE_LABELS:
        if not frappe.db.exists("Workspace", label):
            continue

        doc = frappe.get_doc("Workspace", label)
        safe_set(doc, "parent_page", "KSA HR Platform")
        safe_set(doc, "is_hidden", 1)
        safe_set(doc, "public", 1)
        doc.save(ignore_permissions=True)


def build_workspace_content(workspace):
    blocks = [
        {
            "type": "header",
            "data": {"text": workspace["title"], "col": 12},
        },
        {
            "type": "paragraph",
            "data": {"text": workspace["headline"], "col": 12},
        },
        {
            "type": "paragraph",
            "data": {"text": workspace["description"], "col": 12},
        },
        {
            "type": "spacer",
            "data": {"col": 12},
        },
    ]

    for section in workspace["sections"]:
        blocks.append(
            {
                "type": "header",
                "data": {"text": section["title"], "col": 12},
            }
        )
        blocks.append(
            {
                "type": "paragraph",
                "data": {"text": section["description"], "col": 12},
            }
        )
        blocks.append(
            {
                "type": "paragraph",
                "data": {"text": "DocTypes: " + join_section_labels(section) + ".", "col": 12},
            }
        )

    return blocks


def build_workspace_links(workspace):
    rows = []
    for section in workspace["sections"]:
        rows.append(
            {
                "type": "Card Break",
                "label": section["title"],
                "hidden": 0,
                "onboard": 0,
                "link_count": 0,
            }
        )
        for link_to, label in section["items"]:
            rows.append(
                {
                    "type": "Link",
                    "label": label,
                    "link_type": "DocType",
                    "link_to": link_to,
                    "onboard": 1,
                    "hidden": 0,
                    "is_query_report": 0,
                    "link_count": 0,
                }
            )
    return rows


def build_workspace_shortcuts(workspace):
    rows = []
    for section in workspace["sections"]:
        for link_to, label in section["items"]:
            rows.append(
                {
                    "shortcut_name": label,
                    "label": label,
                    "type": "DocType",
                    "link_type": "DocType",
                    "link_to": link_to,
                    "doc_view": "List",
                    "color": "Blue",
                }
            )
    return rows


def set_workspace_child_rows(doc, fieldname, rows):
    if not doc.meta.has_field(fieldname):
        return

    doc.set(fieldname, [])
    child_fields = get_child_fields(doc, fieldname)

    for row in rows:
        if child_fields:
            row = {field: value for field, value in row.items() if field in child_fields}
        doc.append(fieldname, row)


def get_child_fields(doc, fieldname):
    field = doc.meta.get_field(fieldname)
    child_doctype = getattr(field, "options", None)
    if not child_doctype or not frappe.db.exists("DocType", child_doctype):
        return set()

    return {field.fieldname for field in frappe.get_meta(child_doctype).fields}


def join_section_labels(section):
    return "; ".join(label for _, label in section["items"])


def safe_set(doc, fieldname, value):
    if doc.meta.has_field(fieldname):
        doc.set(fieldname, value)
