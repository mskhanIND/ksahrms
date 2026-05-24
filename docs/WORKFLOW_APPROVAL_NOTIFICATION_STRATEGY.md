# Workflow, Approval, And Notification Strategy

## Current Status

The clean app has process blueprints but does not yet contain implemented workflows, notification records, email templates, or approval DocTypes. These must be built during implementation.

## Design Target

Every operational DocType should have:

- A clear process owner.
- A lifecycle state field.
- A workflow state model.
- A role-based approval path.
- Email notifications for important state changes.
- Audit-friendly comments and timestamps.
- Reports or dashboards for pending work.

## Shared Workflow States

Use shared states unless a process needs something more specific:

- Draft
- Submitted
- Pending Approval
- More Information Required
- Approved
- Rejected
- In Progress
- Completed
- Cancelled

Payroll, settlement, and accrual processes may add:

- Payroll Review
- Finance Review
- Final Approval
- Posted
- Reconciled

## Approval Matrix

Create one owned approval engine instead of hard-coding approvals in every DocType.

Recommended DocTypes:

- Approval Matrix
- Approval Matrix Rule
- Approval Step
- Delegation Rule

Rule inputs:

- Company
- Department
- Branch
- Employee grade
- Request type
- Amount
- Currency
- Cost center
- Role
- Employment type

Rule outputs:

- Required approver role.
- Required approver user.
- Approval order.
- Escalation time.
- Whether finance approval is required.
- Whether HR manager approval is required.

## Email Notification Strategy

Create reusable notification templates and call them from workflow transitions.

Core notification moments:

- Document submitted.
- Approval assigned.
- Approval reminder.
- Rejection.
- More information requested.
- Approval completed.
- Fulfilment task assigned.
- SLA breached.
- Process completed.

Suggested templates:

- Approval Required
- Request Submitted
- Request Rejected
- More Information Required
- Task Assigned
- SLA Reminder
- Completion Notice
- Exception Alert

## Role Strategy

Recommended roles:

- Employee Self Service
- Line Manager
- HR User
- HR Manager
- Payroll User
- Payroll Manager
- Finance User
- Finance Manager
- Compliance Officer
- System Manager

## Process Ownership

Each DocType must have one process owner:

- HR owns employee, service, recruitment, compliance, clearance, and policy records.
- Payroll owns payroll-impacting adjustments and payroll run controls.
- Finance owns accruals, journal proposals, payments, and accounting validation.
- Managers own business approval and operational confirmations.

## Implementation Order

1. Create roles.
2. Create Approval Matrix DocTypes.
3. Create Email Template records.
4. Create Notification records.
5. Create Workflow records.
6. Link workflow transitions to notification logic.
7. Add dashboards for pending approvals.
8. Add tests for each workflow path.

## Definition Of Done

A process is complete only when:

- A user knows where to start.
- The document moves through expected states.
- The correct approver receives the request.
- Rejection and resubmission work.
- Email notifications are sent at the right points.
- Reports show pending and overdue work.
- Permissions prevent unauthorized approvals.

