from __future__ import annotations

import frappe


FALLBACK_STEPS = [
    ("Line Manager Review", "Line Manager"),
    ("HR Review", "HR Manager"),
    ("Finance Review", "Finance Manager"),
]


def get_approval_plan(doc) -> list[dict]:
    matrix = find_best_matrix(doc)
    if matrix:
        return [
            {
                "sequence": row.sequence,
                "approval_stage": row.approval_stage,
                "approver_role": row.approver_role,
                "approver_user": row.approver_user,
                "status": "Pending",
            }
            for row in matrix.approval_steps
            if row.required
        ]

    return fallback_plan_from_service(doc)


def find_best_matrix(doc):
    matrix_names = frappe.get_all(
        "Approval Matrix",
        filters={"disabled": 0, "applies_to_doctype": doc.doctype},
        fields=["name"],
        order_by="priority asc, modified desc",
    )

    best = None
    best_score = -1
    for row in matrix_names:
        matrix = frappe.get_doc("Approval Matrix", row.name)
        score = score_matrix(matrix, doc)
        if score > best_score:
            best = matrix
            best_score = score

    return best


def score_matrix(matrix, doc) -> int:
    score = 0
    if matrix.company:
        if matrix.company != doc.company:
            return -1
        score += 2
    if matrix.service:
        if matrix.service != doc.service:
            return -1
        score += 4
    if matrix.department:
        if matrix.department != doc.department:
            return -1
        score += 3
    if matrix.min_amount and (not doc.amount or doc.amount < matrix.min_amount):
        return -1
    if matrix.max_amount and doc.amount and doc.amount > matrix.max_amount:
        return -1
    if matrix.min_amount or matrix.max_amount:
        score += 1
    return score


def fallback_plan_from_service(doc) -> list[dict]:
    service = frappe.get_cached_doc("Service Catalog", doc.service)
    configured = []
    if service.requires_line_manager:
        configured.append(FALLBACK_STEPS[0])
    if service.requires_hr_manager:
        configured.append(FALLBACK_STEPS[1])
    if service.requires_finance:
        configured.append(FALLBACK_STEPS[2])
    if not configured:
        configured.append(("HR Review", "HR Manager"))

    return [
        {
            "sequence": index,
            "approval_stage": stage,
            "approver_role": role,
            "status": "Pending",
        }
        for index, (stage, role) in enumerate(configured, start=1)
    ]
