# First Slice Test Plan

Use this after installing the app on a bench site.

## 1. Installation Checks

- Install the app.
- Run migrate.
- Confirm these DocTypes exist:
  - HR Platform Settings
  - HR Process Guide
  - HR Process Guide Item
  - Approval Matrix
  - Approval Matrix Step
  - Service Catalog
  - Employee Service Request
  - Employee Service Request Approval
  - Service Fulfilment Task
  - Employee HR Profile
  - Hiring Request
  - Attendance Exception
  - Leave Benefit Request
  - Payroll Adjustment
  - Exit Case
  - Accrual Policy
  - Compliance Alert
- Confirm these workspaces exist:
  - KSA HR Platform
  - KSA HR Settings
  - KSA Employee Services
  - KSA Workforce Core
  - KSA Recruitment Onboarding
  - KSA Attendance Time
  - KSA Leave Benefits
  - KSA Payroll Compensation
  - KSA Offboarding Settlement
  - KSA Accruals Finance
  - KSA Analytics Compliance
- Confirm these roles exist:
  - Employee Self Service
  - Line Manager
  - HR User
  - HR Manager
  - Finance User
  - Finance Manager

## 2. Settings Checks

- Open HR Platform Settings.
- Open HR Process Guide and review Start Here.
- Confirm Employee Service Request Series is set.
- Confirm default SLA hours are set.
- Confirm email notifications are enabled only if outgoing email is configured.

## 3. Service Catalog Checks

- Confirm default services exist:
  - HR Letter Request
  - Travel Request
  - Asset Request
  - Insurance Service Request
  - Payment Request
- Create one custom service with line manager and HR approvals.

## 4. Request Workflow Checks

- Create an Employee Service Request.
- Select a Service Catalog item.
- Select an Employee.
- Add subject and description.
- Save and submit.
- Confirm approval rows are generated.
- Confirm Process Status moves to the first pending approval stage.
- Approve the current step.
- Continue until approvals are complete.
- Confirm a fulfilment task is created.
- Mark the request completed.
- Confirm Process Status is Completed.

## 5. Negative Checks

- Try a Payment Request without amount and confirm validation blocks it.
- Try approving with a user that does not have the required role.
- Reject a pending request and confirm the request status becomes Rejected.

## 6. Not Yet Covered

- Full Frappe Workflow fixture records.
- Dashboard cards for pending approvals.
- Scheduled SLA reminder emails.
- Employee self-service portal pages.
- Production data migration.
