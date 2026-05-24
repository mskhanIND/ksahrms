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
        "process_name": "Hire To Join",
        "module": "Recruitment Onboarding",
        "status": "Planned",
        "owner_role": "HR Manager",
        "start_point": "Department raises hiring need or replacement request.",
        "end_point": "Employee record is active, joining checklist is complete, and probation review is scheduled.",
        "workflow_summary": "Workforce Plan -> Hiring Request -> Candidate -> Offer -> Joining -> Probation.",
        "approval_strategy": "Department Head, HR, Finance where budget applies, and authorized offer approver.",
        "notification_strategy": "Hiring approval, interview scheduling, offer approval, joining checklist, and probation reminders.",
        "next_action": "Build Workforce Plan and Hiring Request in a later slice.",
        "related_doctypes": []
    },
    {
        "sequence": 4,
        "process_name": "Time To Pay",
        "module": "Attendance Time",
        "status": "Planned",
        "owner_role": "Payroll Manager",
        "start_point": "Attendance, leave, shift, overtime, or exception data enters the month.",
        "end_point": "Payroll-impacting adjustments are approved and included in payroll run controls.",
        "workflow_summary": "Device Sync -> Attendance Exception -> Approval -> Payroll Adjustment -> Payroll Run.",
        "approval_strategy": "Line Manager validates exceptions, HR validates policy, Payroll validates salary impact.",
        "notification_strategy": "Device sync failures, pending overtime/exception approvals, and payroll readiness alerts.",
        "next_action": "Build Time Device, Attendance Exception, and Payroll Adjustment in a later slice.",
        "related_doctypes": []
    },
    {
        "sequence": 5,
        "process_name": "Exit To Settlement",
        "module": "Offboarding Settlement",
        "status": "Planned",
        "owner_role": "HR Manager",
        "start_point": "Resignation, termination, final exit, or contract-end action is initiated.",
        "end_point": "Clearance is complete, final settlement is approved, and payment/accounting records are posted.",
        "workflow_summary": "Exit Case -> Clearance -> EOS Calculation -> Payroll Review -> Finance Review -> Settled.",
        "approval_strategy": "HR validates policy, departments confirm clearance, Payroll validates dues, Finance validates payment.",
        "notification_strategy": "Clearance assignment, overdue clearance, settlement approval, and completion notices.",
        "next_action": "Build Exit Case and Clearance Checklist in a later slice.",
        "related_doctypes": []
    },
    {
        "sequence": 6,
        "process_name": "Accrual To Journal",
        "module": "Accruals Finance",
        "status": "Planned",
        "owner_role": "Finance Manager",
        "start_point": "Monthly accrual schedule becomes due.",
        "end_point": "Journal proposal is reviewed, posted, and reconciled.",
        "workflow_summary": "Accrual Policy -> Calculation Batch -> Journal Proposal -> Posted -> Reconciled.",
        "approval_strategy": "HR validates employee assumptions. Finance validates accounts, cost centers, and journals.",
        "notification_strategy": "Schedule due, calculation completed, journal posting failed, and reconciliation pending.",
        "next_action": "Build Accrual Policy and Accrual Journal Proposal in a later slice.",
        "related_doctypes": []
    }
]

WORKSPACES = [
    {
        "label": "KSA HR Platform",
        "title": "KSA HR Platform",
        "module": "HR Settings",
        "sequence_id": 1,
        "headline": "Start here: configure HR Settings, then run Employee Service Requests.",
        "description": "This workspace shows the current implemented slice and the planned end-to-end HR process map.",
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
        safe_set(doc, "sequence_id", workspace["sequence_id"])
        safe_set(doc, "indicator_color", "green")
        safe_set(doc, "icon", "organization")

        if doc.meta.has_field("content"):
            doc.content = json.dumps(build_workspace_content(workspace))

        if doc.meta.has_field("links"):
            doc.set("links", [])
            for link_to, label in workspace["links"]:
                doc.append(
                    "links",
                    {
                        "type": "Link",
                    "label": label,
                    "link_type": "DocType",
                    "link_to": link_to,
                    "onboard": 1,
                    "hidden": 0,
                    "is_query_report": 0,
                    "link_count": 0,
                },
            )

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

    for link_to, label in workspace["links"]:
        blocks.append(
            {
                "type": "shortcut",
                "data": {
                    "shortcut_name": label,
                    "label": label,
                    "link_to": link_to,
                    "type": "DocType",
                    "col": 3,
                },
            }
        )

    return blocks


def safe_set(doc, fieldname, value):
    if doc.meta.has_field(fieldname):
        doc.set(fieldname, value)
