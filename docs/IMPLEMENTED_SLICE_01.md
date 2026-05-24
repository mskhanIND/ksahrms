# Implemented Slice 01

This slice turns the clean scaffold into the first usable HR process foundation.

## Included

- HR Platform Settings
- HR Process Guide
- HR Process Guide Item
- Approval Matrix
- Approval Matrix Step
- Service Catalog
- Employee Service Request
- Employee Service Request Approval
- Service Fulfilment Task
- KSA HR Platform workspace records
- Foundation process-owner DocTypes:
  - Employee HR Profile
  - Hiring Request
  - Attendance Exception
  - Leave Benefit Request
  - Payroll Adjustment
  - Exit Case
  - Accrual Policy
  - Compliance Alert

## First User Path

1. Open the `KSA HR Platform` workspace.
2. Open `HR Process Guide` and read `Start Here`.
3. Review `HR Platform Settings`.
4. Review or create `Service Catalog` records.
5. Optionally create `Approval Matrix` rules.
6. Create an `Employee Service Request`.
7. Submit it.
8. Approve each pending step.
9. Complete the fulfilment task.

## What Works

- Service catalog driven request defaults.
- Approval plan generation from Approval Matrix.
- Fallback approval plan from Service Catalog.
- Submitted request approval and rejection actions.
- Fulfilment task creation after approvals.
- Completion action.
- Email notification service hook for submitted, approved, rejected, and completed events.
- Workspaces for KSA HR Platform, HR Settings, and Employee Services.
- Workspaces for every process module so no module opens empty.
- In-app process guide records for available and planned process slices.

## Still To Build

- Full Frappe Workflow fixture records.
- Dashboards for pending approvals and overdue requests.
- SLA reminder scheduler.
- Employee self-service portal pages.
- Tests inside a bench site.
- Migration scripts from old apps.

Use `FIRST_SLICE_TEST_PLAN.md` for the first bench installation test.
