# Readiness Gates

The clean app is ready only when each gate below passes. Static source coverage is necessary, but it is not enough.

## 1. Scope Coverage

- Every source DocType is mapped to one target process or explicitly retired.
- Every source hook, script, report, print format, notification, and patch is mapped to rebuild, migrate, replace, or retire.
- Every duplicate is resolved by a named target owner.

## 2. Technical Install

- App installs on a fresh bench site.
- `bench migrate` completes without missing imports, missing assets, fixture errors, or duplicate DocType errors.
- All hook paths resolve.
- All public assets build and load.

## 3. Process Implementation

- Hire to Join works end to end.
- Time to Pay works end to end.
- Request to Approval works end to end.
- Exit to Settlement works end to end.
- Accrual to Journal works end to end.
- Compliance alerts and dashboards work end to end.

## 4. Data Migration

- Migration dry-run completes on a copy of production data.
- Source and target record counts reconcile.
- Submitted payroll, accounting, and settlement records are preserved.
- Open approvals and transactions are migrated with clear ownership.

## 5. Security And Controls

- Roles, permissions, workflows, and approval limits are reviewed.
- HR, payroll, finance, employee self-service, and system manager access are separated.
- Audit trail requirements are confirmed.

## 6. User Acceptance

- HR validates employee services, recruitment, attendance exceptions, leave, and offboarding.
- Payroll validates salary, benefits, bank transfer, and settlement output.
- Finance validates accruals, invoices, journal entries, and payments.
- Management validates dashboards and alerts.

## Current Status

The current clean app now includes the first foundation slice: HR Platform Settings, Approval Matrix, Service Catalog, Employee Service Request, approval rows, fulfilment tasks, and email notification service hooks.

It is ready for controlled bench installation and implementation testing. It is not ready for production use until all readiness gates pass.
