import json

import frappe

from ksa_hr_platform.setup.onboarding import WORKSPACE_SECTIONS


WORKSPACE_NAME = "KSA HR Platform"


def update_clickable_workspace():
    if not frappe.db.exists("DocType", "Workspace"):
        return

    if not frappe.db.exists("Workspace", WORKSPACE_NAME):
        return

    doc = frappe.get_doc("Workspace", WORKSPACE_NAME)
    safe_set(doc, "label", WORKSPACE_NAME)
    safe_set(doc, "title", WORKSPACE_NAME)
    safe_set(doc, "module", "HR Settings")
    safe_set(doc, "public", 1)
    safe_set(doc, "is_hidden", 0)
    safe_set(doc, "parent_page", "")
    safe_set(doc, "indicator_color", "green")
    safe_set(doc, "icon", "organization")

    if doc.meta.has_field("content"):
        doc.content = json.dumps(build_content())

    set_child_rows(doc, "links", build_links())
    set_child_rows(doc, "shortcuts", build_shortcuts())
    doc.save(ignore_permissions=True)
    frappe.clear_cache(doctype="Workspace")


def build_content():
    blocks = [
        {
            "type": "header",
            "data": {"text": '<span class="h4"><b>KSA HR Platform</b></span>', "col": 12},
        },
        {
            "type": "paragraph",
            "data": {
                "text": "Start here: configure HR Settings, then run Employee Service Requests.",
                "col": 12,
            },
        },
        {
            "type": "header",
            "data": {"text": '<span class="h4"><b>Start Here</b></span>', "col": 12},
        },
    ]

    for _, label in WORKSPACE_SECTIONS[0]["items"]:
        blocks.append({"type": "shortcut", "data": {"shortcut_name": label, "col": 3}})

    blocks.extend(
        [
            {"type": "spacer", "data": {"col": 12}},
            {
                "type": "header",
                "data": {"text": '<span class="h4"><b>Process Areas</b></span>', "col": 12},
            },
        ]
    )

    for section in WORKSPACE_SECTIONS:
        blocks.append(
            {
                "type": "card",
                "data": {"card_name": section["title"], "col": 4},
            }
        )

    return blocks


def build_links():
    rows = []

    for section in WORKSPACE_SECTIONS:
        rows.append(
            {
                "type": "Card Break",
                "label": section["title"],
                "link_to": None,
                "link_type": None,
                "hidden": 0,
                "onboard": 0,
                "link_count": len(section["items"]),
            }
        )

        for link_to, label in section["items"]:
            rows.append(
                {
                    "type": "Link",
                    "label": label,
                    "link_type": "DocType",
                    "link_to": link_to,
                    "onboard": 0,
                    "hidden": 0,
                    "is_query_report": 0,
                    "link_count": 0,
                }
            )

    return rows


def build_shortcuts():
    rows = []

    for section in WORKSPACE_SECTIONS:
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


def set_child_rows(doc, fieldname, rows):
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


def safe_set(doc, fieldname, value):
    if doc.meta.has_field(fieldname):
        doc.set(fieldname, value)
