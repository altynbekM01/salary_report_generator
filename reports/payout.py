def generate_payout_report(employees):
    lines = ["Отчет по зарплате для каждого сотрудника"]
    header = f"{'Name':<20} {'Department':<15} {'Hours':<10} {'Rate':<10} {'Payout':<10}"
    lines.append(header)
    lines.append("-" * len(header))

    for emp in employees:
        lines.append(f"{emp.name:<20} {emp.department:<15} {emp.hours_worked:<10} {emp.hourly_rate:<10} {emp.payout():<10.2f}")

    return "\n".join(lines)
