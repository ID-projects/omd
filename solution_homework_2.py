import csv
from collections import defaultdict


def read_data(file_path):
    teams = defaultdict(set)
    employee_counts = defaultdict(int)
    salaries = defaultdict(list)

    with open(file_path, "r", encoding="utf-8-sig", newline="") as file:
        reader = csv.DictReader(file, delimiter=";")

        for row in reader:
            department = row["Департамент"]
            team = row["Отдел"]
            salary = float(row["Оклад"])

            teams[department].add(team)
            employee_counts[department] += 1
            salaries[department].append(salary)

    return teams, employee_counts, salaries


def make_summary(employee_counts, salaries):
    summary = []

    for department in employee_counts:
        department_salaries = salaries[department]

        summary.append({
            "Департамент": department,
            "Количество сотрудников": employee_counts[department],
            "Минимальная зарплата": min(department_salaries),
            "Максимальная зарплата": max(department_salaries),
            "Средняя зарплата": (
                sum(department_salaries) / len(department_salaries)
            ),
        })

    return summary


def hierarchy_report(teams):
    for department in teams:
        print(f"{department}:")
        for team in teams[department]:
            print(f"  - {team}")


def summary_report(summary):
    for row in summary:
        print(
            f"{row['Департамент']}: "
            f"сотрудников — {row['Количество сотрудников']}, "
            f"минимальная зарплата — {row['Минимальная зарплата']}, "
            f"максимальная — {row['Максимальная зарплата']}, "
            f"средняя — {row['Средняя зарплата']}"
        )


def save_summary_report(summary, output_file):
    fieldnames = [
        "Департамент",
        "Количество сотрудников",
        "Минимальная зарплата",
        "Максимальная зарплата",
        "Средняя зарплата",
    ]

    with open(output_file, "w", encoding="utf-8-sig", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames, delimiter=";")
        writer.writeheader()
        writer.writerows(summary)

    print(f"Отчёт сохранён в файл: {output_file}")


def create_report(
    report_type: int,
    input_file="Corp_Summary.csv",
    output_file="Department_summary.csv",
):
    if report_type not in (1, 2, 3):
        raise ValueError("report_type должен быть 1, 2 или 3")

    teams, employee_counts, salaries = read_data(input_file)

    if report_type == 1:
        hierarchy_report(teams)
    elif report_type == 2:
        summary_report(make_summary(employee_counts, salaries))
    elif report_type == 3:
        save_summary_report(
            make_summary(employee_counts, salaries), output_file
        )


if __name__ == "__main__":
    create_report(3)