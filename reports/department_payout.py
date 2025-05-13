from models import Employee
from collections import defaultdict


def generate_department_payout_report(employees: list[Employee]) -> str:
    dept_totals = defaultdict(float)
    for emp in employees:
        dept_totals[emp.department] += emp.payout()

    lines = ["Отчет по зарплате департаментов:"]
    for dept, total in sorted(dept_totals.items()):
        lines.append(f"{dept}: {total:.2f}")
    return "\n".join(lines)