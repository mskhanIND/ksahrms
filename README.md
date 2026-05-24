# KSA HR Platform

KSA HR Platform is a fresh, process-oriented Frappe app for Saudi HR operations.

The app is intentionally built under one owned namespace: `ksa_hr_platform`. It does not copy legacy app packages, hook paths, module names, or runtime dependencies. Existing HR apps should be used only as requirement references while rebuilding the product with a cleaner process model.

## Product Direction

- One app namespace and one hook surface.
- Process-first modules instead of vendor/source-app modules.
- ERPNext and HRMS remain platform dependencies; old custom apps do not.
- Integrations are wrapped behind owned services so business logic stays controllable.
- Duplicate DocTypes and overrides are replaced by explicit process owners.

## Main Processes

- Hire to Join
- Time to Pay
- Request to Approval
- Exit to Settlement
- Accrual to Journal
- Compliance to Action

## Next Build Step

Start with HR Settings, Workforce Core, and the shared approval/request framework. Then implement the operational processes in thin vertical slices so every release is usable.

## After Install

Read `docs/START_HERE_AFTER_INSTALL.md` first. The current package is a clean implementation scaffold, not a production-ready HRMS. Use the readiness gates and process lifecycle matrix before enabling real users.
