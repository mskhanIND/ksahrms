# Implemented Slice 01

This slice turns the clean scaffold into the first usable HR process foundation.

## Included

- HR Platform Settings
- Approval Matrix
- Approval Matrix Step
- Service Catalog
- Employee Service Request
- Employee Service Request Approval
- Service Fulfilment Task

## First User Path

1. Open HR Settings.
2. Review HR Platform Settings.
3. Review or create Service Catalog records.
4. Optionally create Approval Matrix rules.
5. Create an Employee Service Request.
6. Submit it.
7. Approve each pending step.
8. Complete the fulfilment task.

## What Works

- Service catalog driven request defaults.
- Approval plan generation from Approval Matrix.
- Fallback approval plan from Service Catalog.
- Submitted request approval and rejection actions.
- Fulfilment task creation after approvals.
- Completion action.
- Email notification service hook for submitted, approved, rejected, and completed events.

## Still To Build

- Full Frappe Workflow fixture records.
- Dashboards for pending approvals and overdue requests.
- SLA reminder scheduler.
- Employee self-service portal pages.
- Tests inside a bench site.
- Migration scripts from old apps.

Use `FIRST_SLICE_TEST_PLAN.md` for the first bench installation test.
