"""List tipidagi strkturani 20ta random sonlar bilan to’ldiruvchi va shu sonlar yig’indisini aniqlab 
list oxiriga quyidagi ko’rinishda qo’shuvchi dastur tuzing.
[93, 91, 70, 43, 67, 62, 44, 73, 43, 59, 26, 89, 16, 98, 15, 92, 93, 91, 45, 79]
[93, 91, 70, 43, 67, 62, 44, 73, 43, 59, 26, 89, 16, 98, 15, 92, 93, 91, 45, 79, 'SUM: 1289']
"""
import random

randomsonlar = [random.randint(1, 100) for _ in range(20)]
yigindi = sum(randomsonlar)
randomsonlar.append(f'SUM: {yigindi}')
print(randomsonlar)
