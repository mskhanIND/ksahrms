# Control Boundaries

The purpose of this rebuild is control. The platform should own process decisions and use ERPNext/HRMS for stable accounting, payroll, employee, attendance, and leave records.

## Owned by KSA HR Platform

- Saudi HR policy configuration.
- Employee service request lifecycle.
- Clearance and settlement orchestration.
- Accrual calculation workflow.
- Device sync orchestration.
- Compliance dashboards and alerts.

## Owned by ERPNext/HRMS

- Core Employee records.
- Attendance and Employee Checkin final records.
- Leave Application and Leave Allocation final records.
- Salary Slip and Payroll Entry final records.
- Journal Entry and Payment Entry final records.

## Integration Rule

Owned DocTypes prepare, validate, and orchestrate. Standard ERPNext/HRMS DocTypes remain the final system of record where they already have mature accounting or HR behaviour.
