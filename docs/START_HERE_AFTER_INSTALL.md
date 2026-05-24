# Start Here After Install

## Current Truth

Installing `ksa_hr_platform` today gives you the clean app shell plus the first implementation slice: HR Platform Settings, Approval Matrix, Service Catalog, Employee Service Request, approval rows, fulfilment tasks, and an email notification service hook. It does not yet give you a production-ready HRMS with every historical process fully rebuilt, dashboards, migration scripts, and UAT-tested permissions.

The app is ready to start controlled implementation. It is not ready to run live HR operations.

## First Screen Mental Model

The user should not start from an old app name. The user should start from the HR process they want to run.

1. HR Settings
2. Workforce Core
3. Recruitment Onboarding
4. Employee Services
5. Attendance Time
6. Leave Benefits
7. Payroll Compensation
8. Offboarding Settlement
9. Accruals Finance
10. Analytics Compliance

## Starting Point

Start with `HR Settings`.

This is where the platform must define:

- Company HR policy.
- Approval matrix.
- Role matrix.
- Service catalog.
- Naming series.
- Email templates.
- Notification rules.
- Integration settings.
- Payroll and finance control settings.

Without HR Settings, every other process becomes hard-coded and difficult to control.

## First Build Sequence

1. Review `HR Platform Settings`.
2. Review the default roles created during install.
3. Review or adjust `Service Catalog` records.
4. Create `Approval Matrix` rules only where service defaults are not enough.
5. Create an `Employee Service Request`.
6. Submit it.
7. Approve the pending steps.
8. Complete the fulfilment task.
9. Add dashboards, SLA reminders, service-specific child tables, and tests.
10. Repeat process by process.

## First Complete Vertical Slice

The recommended first usable release is:

`Employee Service Request -> Approval Matrix -> HR Fulfilment Task -> Email Notification -> Completion`

This proves the core pattern for most HR services such as letters, visa requests, insurance updates, travel requests, asset requests, and payment requests.

## Ending Point

The rebuild is complete only when these end-to-end processes work:

- Hire to Join
- Time to Pay
- Request to Approval
- Exit to Settlement
- Accrual to Journal
- Compliance to Action

Each process must have:

- Owned DocTypes.
- Clear workflow states.
- Role-based approvals.
- Email notifications.
- Reports or dashboards.
- Migration mapping from the old source data.
- UAT signoff from the business owner.

## What Not To Do

- Do not install the old custom apps as dependencies.
- Do not copy old DocTypes directly unless they have been redesigned into the new process.
- Do not rebuild every source DocType one by one.
- Do not start with payroll override code before the approval and settings foundation exists.
- Do not treat this scaffold as production-ready.

## How To Know You Are Ready

Use `docs/READINESS_GATES.md`. The app is ready only when all gates pass.
