#Report Generator

Это приложение на Python для подсчёта заработной платы сотрудников и департаментов на основе данных из CSV-файлов. Позволяет формировать как детализированные отчёты по каждому сотруднику, так и сводные отчёты по подразделениям. Все отчёты выводятся прямо в терминал.
## 🚀 Установка и запуск



1. Клонируйте репозиторий:
```
git clone https://github.com/altynbekM01/salary_report_generator.git
```
2. Создайте и активируйте виртуальное окружение

```
python -m venv venv
source venv/bin/activate  # для Linux/macOS
.\venv\Scripts\activate   # для Windows
```

3. Установите зависимости:
```
pip install -r requirements.txt
```
**Доступные типы отчётов**

**payout** — подробный отчёт по каждому сотруднику, сгруппированный по департаментам.

**department_payout** — Отчёт с суммарной зарплатой по каждому департаменту.

Генерация отчёта по заработной плате каждого сотрудника
```
python main.py file.csv --report payout
```
Где file.csv название вашего файла
Можно указать несколько CSV-файлов:


Генерация отчёта по общей заработной плате для каждого департамента
```
python main.py file1.csv file2.csv --report department_payout
```
Где file.csv название вашего файла
Можно указать несколько CSV-файлов:


📌 Пример CSV-файла 
```
id,email,name,department,hours_worked,salary
1,test1@mail.com,Alice,IT,160,50
2,test2@mail.com,Bob,IT,150,40
3,test3@mail.com,Carol,HR,170,60
```

🧾 Пример вывода отчёта payout
```
Name                 Department      Hours      Rate       Payout    
--------------------------------------------------------------
Alice                IT              160        50         8000.00   
Bob                  IT              150        40         6000.00     
Carol                HR              170        60         10200.00
```

🧾 Пример вывода отчёта department_payout
```
HR: 10200.00
IT: 14000.00
```

Проект покрыт юнит-тестами. Для запуска тестов: pytest

⚙️ Гибкость и расширяемость
Распознавание различных названий колонок через HEADER_MAP в reader.py.

Пример HEADER_MAP:
```
HEADER_MAP = {
    "hourly_rate": "hourly_rate",
    "rate": "hourly_rate",
    "salary": "hourly_rate",
    "hours_worked": "hours_worked",
    "department": "department",
    "name": "name",
}
```

Легкое добавление новых типов отчётов через reports/__init__.py.
