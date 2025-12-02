users = []

for i in range(1):
    print(f"{i+1}- ma'lumotlarini kiriting:")
    fullname = input("To'liq ism: ")
    age = int(input("Yosh: "))
    salary = float(input("Maosh: "))
    
    user = {
        "fullname": fullname,
        "age": age,
        "salary": salary
    }
    users.append(user)

users_sorted = sorted(users, key=lambda x: x["age"])

print("\nFoydalanuvchilar yosh bo'yicha tartiblangan holda:")
for user in users_sorted:
    print(user)
