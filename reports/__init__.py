from reports import payout, department_payout

reports_map = {
    "payout": payout.generate_payout_report,
    "department_payout": department_payout.generate_department_payout_report,
}
