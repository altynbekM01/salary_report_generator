from models import Employee
from utils import HEADER_MAP

def parse_csv(path: str) -> list[Employee]:
    employees = []
    with open(path, encoding="utf-8") as f:
        lines = f.read().strip().splitlines()
        headers = lines[0].split(",")
        normalized_headers = [HEADER_MAP.get(h.strip(), h.strip()) for h in headers]

        for row in lines[1:]:
            values = row.split(",")
            data = dict(zip(normalized_headers, values))
            employee = Employee(
                name=data["name"],
                department=data["department"],
                hours_worked=float(data["hours_worked"]),
                hourly_rate=float(data["hourly_rate"]),
            )
            employees.append(employee)
    return employees
