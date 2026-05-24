# Process Architecture

            The platform is organized by HR process ownership, not by the names of earlier apps. Each process has one primary module, one set of owned DocTypes, and explicit touchpoints with ERPNext/HRMS.

            ## Principles

            - Keep one namespace: `ksa_hr_platform`.
            - Keep one hook surface: `ksa_hr_platform.hooks`.
            - Own process state in new DocTypes instead of inheriting duplicate custom DocTypes.
            - Extend ERPNext/HRMS only at stable boundaries.
            - Put external devices, payroll side effects, accounting side effects, and notifications behind services.
            - Prefer a shared request and approval model over many unrelated request DocTypes.

            ## Modules

            | Module | Package | Responsibility |
            | --- | --- | --- |
            | Workforce Core | `workforce_core` | Employee master data, contracts, dependents, documents, positions, grades, and organization structure. |
| Recruitment Onboarding | `recruitment_onboarding` | Manpower planning, recruitment requests, candidate selection, offers, joining, and probation. |
| Attendance Time | `attendance_time` | Device integration boundaries, check-ins, shifts, attendance adjustments, overtime, and time exceptions. |
| Leave Benefits | `leave_benefits` | Leave entitlement, vacations, work resumption, leave dues, permissions, tickets, and benefit eligibility. |
| Payroll Compensation | `payroll_compensation` | Salary structures, payroll runs, payroll effects, bank transfers, payroll accounting, and payslip extensions. |
| Employee Services | `employee_services` | Employee self-service requests, approvals, letters, visas, insurance, travel, assets, and payments. |
| Offboarding Settlement | `offboarding_settlement` | Resignation, termination, clearance, end-of-service benefits, gratuity, final settlement, and exits. |
| Accruals Finance | `accruals_finance` | Monthly provisions, recurring accruals, journal entry creation, finance controls, and reconciliation. |
| Analytics Compliance | `analytics_compliance` | Saudi HR compliance, dashboards, expiry tracking, employee/payroll/attendance reports, and notifications. |
| HR Settings | `hr_settings` | Company-level policies, workflow rules, approval matrices, integrations, numbering, and platform setup. |

            ## End-to-End Processes

            | Process | Modules | First Owned DocTypes |
            | --- | --- | --- |
            | Hire to Join | Recruitment Onboarding, Workforce Core | Workforce Plan, Hiring Request, Candidate Profile, Interview Evaluation, Offer Approval, Joining Checklist, Probation Review |
| Time to Pay | Attendance Time, Leave Benefits, Payroll Compensation | Time Device, Device Sync Batch, Attendance Exception, Shift Change Request, Overtime Request, Leave Benefit Ledger, Payroll Run Control, Payroll Adjustment, Bank Transfer Batch |
| Request to Approval | Employee Services | Employee Service Request, Service Catalog, Service Approval Rule, Service Fulfilment Task, HR Letter Request, Travel Service Request, Asset Service Request, Insurance Service Request |
| Exit to Settlement | Offboarding Settlement, Payroll Compensation, Accruals Finance | Exit Case, Clearance Checklist, Clearance Item, End Of Service Calculation, Final Settlement Run, Settlement Payment Control |
| Accrual to Journal | Accruals Finance | Accrual Policy, Accrual Schedule, Accrual Calculation Batch, Accrual Journal Proposal, Accrual Reconciliation |
