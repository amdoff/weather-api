"""
FizzBuzz algoritmi. Foydalanuvchi son kiritadi. Agar kiritilgan son 3ga qoldiqsiz bo'linsa,
ekranga Fizz yozuvi chiqsin, agar 5 ga qoldiqsiz bo'linsa,
ekranga Buzz yozuvi chiqsin, agar 3 ga ham 5 ga ham qoldiqsiz bo'linsa FizzBuzz yozuvi chiqsin.
"""
a = int (input("biror sonni kiriting:"))
if a % 3 == 0:
    print ("Fizz")
elif a % 5 == 0:
    print("Buzz")
elif a % 3 == 0 and a % 5 == 0:
    print ("FizzBuzz")
else:
    print ("a") 