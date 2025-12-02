"""
Foydalanuvchi `int` tipida bir son kiritadi. Quyidagi shartlar bajarilgan hoatda ekranga
 `True` degan yozuv chiqarilsin, aks holda, dastur to’xtatilsin.

- Kiritilgan son 3 ga yoki 7 qoldiqsiz bo’linishi lozim;
- Kiritilgan son 5 ga qoldiqsiz bo’linishi va 0 bilan tugamasligi lozim.
"""
a = int(input("Sonni kiriting: "))
if (a % 3 == 0 or a % 7 == 0) and ( a % 5 == 0 and a % 10 != 0):
    print(True)
else:
    exit() 