# Migration Strategy

This app is a fresh build. Existing custom apps should not be installed as dependencies of `ksa_hr_platform`.

## Approach

1. Freeze current production behaviour and list active workflows.
2. Map each active workflow to one owned process in this app.
3. Create new DocTypes and services for the target process.
4. Migrate data through explicit import scripts, not copied controllers.
5. Retire old custom apps after process parity is verified.

## Data Migration Rules

- Migrate business records, not source-app implementation details.
- Preserve submitted accounting and payroll documents as historical records.
- Rebuild approval state only when it is needed for open transactions.
- Keep old DocType names out of new user workflows unless they are standard ERPNext/HRMS DocTypes.
- Store source mapping scripts outside the runtime app when possible.

## Dependency Rules

- Allowed platform dependencies: Frappe, ERPNext, HRMS.
- Avoid custom app dependencies.
- Any external integration must be represented by an owned service wrapper.
