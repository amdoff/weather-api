data = [
    {"full_name": "Eugene Elsmor", "company": "Kazu", "position": "Electrical Engineer", "salary": "$4440.86"},
    {"full_name": "Joni Stredder", "company": "JumpXS", "position": "Environmental Tech", "salary": "$870.05"},
    {"full_name": "Wolfy Swanborough", "company": "Topiclounge", "position": "Recruiter", "salary": "$1045.61"},
    {"full_name": "Raleigh Ratter", "company": "Zoozzy", "position": "Graphic Designer", "salary": "$602.41"},
    {"full_name": "Richy Cleft", "company": "Jamia", "position": "Sales Associate", "salary": "$912.98"}
]
for emp in data:
    salary = float(emp["salary"].replace("$", ""))
    if salary < 1000:
        new_salary = salary + 1000
        print(f"NAME: {emp['full_name']}")
        print(f"COMPANY NAME: {emp['company']}")
        print(f"JOB POSITION: {emp['position']}")
        print(f"NEW SALARY: ${new_salary:.2f}")
        print("-" * 30)
