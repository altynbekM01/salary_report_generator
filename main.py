import argparse
from reader import parse_csv
from reports import reports_map

def main():
    parser = argparse.ArgumentParser(description="Salary Report Generator")
    parser.add_argument("files", nargs="+", help="CSV files with employee data")
    parser.add_argument("--report", required=True, help="Report type to generate")

    args = parser.parse_args()

    employees = []
    for file in args.files:
        employees.extend(parse_csv(file))

    report_func = reports_map.get(args.report)

    if report_func:
        report = report_func(employees)
        print(report)
    else:
        print(f"Unknown report type: {args.report}")

if __name__ == "__main__":
    main()
