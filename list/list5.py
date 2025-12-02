"""
List tipidagi strkturani 10ta random sonlar bilan to’ldiruvchi dastur tuzing.
Foydalanuvchi kiritgan son List ichida nechta borligini aniqlovchi shart qo’shing.
"""
import random 
a = [random.randint(1,100)for i in range (10)]
print(a)
b = int(input("son kiriting"))
c = a.count(b)
print(a)
print(f"{b}{c} martda uchradi")
