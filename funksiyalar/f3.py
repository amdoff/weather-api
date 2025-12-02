data = [
    {"full_name": "Eugene Elsmor", "company": "Kazu", "position": "Electrical Engineer", "salary": "$4440.86"},
    {"full_name": "Joni Stredder", "company": "JumpXS", "position": "Environmental Tech", "salary": "$870.05"},
    {"full_name": "Terri-jo Fulham", "company": "Tagchat", "position": "Assistant Media Planner", "salary": "$1992.55"},
    {"full_name": "Priscilla Pandya", "company": "Youopia", "position": "Help Desk Operator", "salary": "$3715.95"},
    {"full_name": "Wolfy Swanborough", "company": "Topiclounge", "position": "Recruiter", "salary": "$1045.61"},
    {"full_name": "Raleigh Ratter", "company": "Zoozzy", "position": "Graphic Designer", "salary": "$602.41"},
    {"full_name": "Anastasia Winward", "company": "Avaveo", "position": "Cost Accountant", "salary": "$3641.42"},
    {"full_name": "Dorry Vasyunichev", "company": "Fivebridge", "position": "Junior Executive", "salary": "$2035.05"},
    {"full_name": "Nollie Phipard-Shears", "company": "Aimbo", "position": "Legal Assistant", "salary": "$3172.57"},
    {"full_name": "Gaynor Dannohl", "company": "Leexo", "position": "Administrative Assistant II", "salary": "$3035.89"},
    {"full_name": "Tome Bensen", "company": "Yamia", "position": "Assistant Professor", "salary": "$3677.10"}
]

assistant_employees = [emp for emp in data if "Assistant" in emp["position"]]
if assistant_employees:
    lowest_paid_assistant = min(assistant_employees, key=lambda x: float(x["salary"].replace("$", "")))
    print(f"NAME: {lowest_paid_assistant['full_name']}")
    print(f"COMPANY NAME: {lowest_paid_assistant['company']}")
    print(f"JOB POSITION: {lowest_paid_assistant['position']}")
    print(f"SALARY: {lowest_paid_assistant['salary']}")
else:
    print("Assistant lavozimida hech kim topilmadi.")
