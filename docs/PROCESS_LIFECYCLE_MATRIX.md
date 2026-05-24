# Process Lifecycle Matrix

This matrix defines the intended starting point, ending point, primary DocTypes, workflow states, approvals, and notification points for each process.

## 1. Hire To Join

Start: A department requests a position or replacement.

End: Employee record is active, joining checklist is completed, and probation tracking is scheduled.

Primary DocTypes:

- Workforce Plan
- Hiring Request
- Candidate Profile
- Interview Evaluation
- Offer Approval
- Joining Checklist
- Probation Review

Workflow:

`Draft -> Department Approval -> HR Review -> Budget Approval -> Recruitment In Progress -> Offer Approval -> Joining In Progress -> Completed`

Approval Strategy:

- Department Head approves need.
- HR validates position, grade, and policy.
- Finance validates budget when required.
- Authorized manager approves offer.

Notifications:

- Hiring request submitted.
- Approval pending.
- Candidate interview scheduled.
- Offer approved or rejected.
- Joining checklist overdue.
- Probation review due.

## 2. Request To Approval

Start: Employee or HR submits a service request.

End: Request is fulfilled, rejected, cancelled, or closed with completion evidence.

Primary DocTypes:

- Service Catalog
- Employee Service Request
- Service Approval Rule
- Service Fulfilment Task
- HR Letter Request
- Travel Service Request
- Asset Service Request
- Insurance Service Request

Workflow:

`Draft -> Submitted -> Line Manager Review -> HR Review -> Finance Review -> Approved -> Fulfilment -> Completed`

Approval Strategy:

- Service Catalog decides which approvals are required.
- Line manager approval is used for employee-impacting requests.
- HR approval is used for policy validation.
- Finance approval is used for paid requests.
- Final fulfilment owner closes the task.

Notifications:

- Request submitted.
- Approval assigned.
- Request rejected.
- More information requested.
- Fulfilment task assigned.
- Request completed.
- SLA breached.

## 3. Time To Pay

Start: Attendance, leave, shift, overtime, or exception data enters the month.

End: Payroll adjustments are approved and included in payroll run controls.

Primary DocTypes:

- Time Device
- Device Sync Batch
- Attendance Exception
- Shift Change Request
- Overtime Request
- Leave Benefit Ledger
- Payroll Run Control
- Payroll Adjustment
- Bank Transfer Batch

Workflow:

`Draft -> Submitted -> Line Manager Review -> HR Time Review -> Payroll Review -> Approved -> Posted To Payroll`

Approval Strategy:

- Manager approves attendance and overtime exceptions.
- HR validates policy and supporting records.
- Payroll validates salary impact.
- Finance validates bank transfer batch where required.

Notifications:

- Device sync failed.
- Attendance exception submitted.
- Overtime pending approval.
- Payroll-impacting adjustment approved.
- Payroll run ready.
- Bank transfer batch ready.

## 4. Exit To Settlement

Start: Employee resignation, termination, final exit, or end-of-contract action is initiated.

End: Clearance is completed, final settlement is approved, and payment/accounting records are posted.

Primary DocTypes:

- Exit Case
- Clearance Checklist
- Clearance Item
- End Of Service Calculation
- Final Settlement Run
- Settlement Payment Control

Workflow:

`Draft -> HR Review -> Department Clearance -> Asset Clearance -> Payroll Review -> Finance Review -> Final Approval -> Settled -> Closed`

Approval Strategy:

- HR validates exit type and policy.
- Department confirms handover.
- Asset owners confirm returns.
- Payroll validates salary, leave, benefits, and deductions.
- Finance validates payment and accounting.
- Authorized signatory approves final settlement.

Notifications:

- Exit case opened.
- Clearance item assigned.
- Clearance overdue.
- EOS calculation ready.
- Settlement pending final approval.
- Settlement completed.

## 5. Accrual To Journal

Start: Monthly accrual policy schedule becomes due.

End: Journal proposal is reviewed, posted, and reconciled.

Primary DocTypes:

- Accrual Policy
- Accrual Schedule
- Accrual Calculation Batch
- Accrual Journal Proposal
- Accrual Reconciliation

Workflow:

`Draft -> Calculated -> HR Review -> Finance Review -> Approved -> Journal Posted -> Reconciled`

Approval Strategy:

- HR validates employee and benefit assumptions.
- Finance validates accounts, cost centers, and amounts.
- Finance Manager approves journal posting.

Notifications:

- Accrual schedule due.
- Calculation completed.
- Review pending.
- Journal posting failed.
- Reconciliation pending.

## 6. Compliance To Action

Start: A compliance condition becomes due or breached, such as document expiry, probation review, iqama expiry, contract expiry, or policy exception.

End: Responsible owner completes the action or closes the risk.

Primary DocTypes:

- Compliance Rule
- Compliance Alert
- Compliance Action
- HR Dashboard Metric

Workflow:

`Open -> Assigned -> In Progress -> Resolved -> Closed`

Approval Strategy:

- HR owns compliance rules.
- Assigned owner handles the action.
- HR Manager closes high-risk actions.

Notifications:

- Upcoming expiry.
- Expiry breached.
- Compliance action assigned.
- Compliance action overdue.
- Compliance action closed.

