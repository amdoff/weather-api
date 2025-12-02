"""
Ikkita son `int` tipida sonlar berilgan berilgan. 
Quyida berilgan shartlar bajarilgan holatda ekranga `TRUE` yozuvi chiqsin. Aks holda `FALSE` chiqarilsin.

- Sonlardan biri juft, ikkinchisi toq bo'lishi kerak.
- Ikkala son ham 3 ga qoldiqsiz bo'linishi kerak.
"""
a = int(input("butun son kiriting:"))
b = int(input("toq son kiriting:"))
if ((a % 2 == 0 and b % 2 == 1) or (a % 2 == 1 and b % 2 == 0)) and (a % 3 == 0 and b % 3 == 0):
    print(True)
else:
     ("False") 