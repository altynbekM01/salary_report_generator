import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from models import Employee


def test_employee_payout():
    emp = Employee(name="Alice", department="IT", hours_worked=160, hourly_rate=50)
    assert emp.payout() == 8000