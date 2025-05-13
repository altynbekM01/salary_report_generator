import pytest
from models import Employee
from reports.payout import generate_payout_report
from reports.department_payout import generate_department_payout_report

# Фейковые данные для сотрудников
@pytest.fixture
def employees():
    emp1 = Employee(name="Alice", department="IT", hours_worked=160, hourly_rate=50)
    emp2 = Employee(name="Bob", department="IT", hours_worked=150, hourly_rate=40)
    emp3 = Employee(name="Carol", department="HR", hours_worked=170, hourly_rate=60)
    return [emp1, emp2, emp3]


def test_generate_department_payout_report(employees):
    report = generate_department_payout_report(employees)
    assert "Отчет по зарплате:" in report
    assert "IT: 14000.00" in report
    assert "HR: 10200.00" in report


def test_generate_payout_report(employees):
    report = generate_payout_report(employees)

    # Проверка на правильную структуру
    assert "Name" in report
    assert "Department" in report
    assert "Hours" in report
    assert "Rate" in report
    assert "Payout" in report

    # Проверка что данные присутсвуют
    assert "Alice" in report
    assert "IT" in report
    assert "160" in report
    assert "50" in report
    assert "8000.00" in report

    assert "Bob" in report
    assert "40" in report
    assert "6000.00" in report

    assert "Carol" in report
    assert "60" in report
    assert "10200.00" in report

