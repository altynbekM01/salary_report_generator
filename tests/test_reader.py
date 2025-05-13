import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from reader import parse_csv

def test_parse_csv(tmp_path):
    data = "id,email,name,department,hours_worked,salary\n" \
           "1,x,x,IT,100,50"
    file = tmp_path / "file.csv"
    file.write_text(data)

    employees = parse_csv(str(file))
    assert len(employees) == 1
    assert employees[0].payout() == 5000
