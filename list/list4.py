"""
List tipidagi strkturani 20ta random sonlar bilan to’ldiruvchi va shu sonlar yig’indisini aniqlab
 list oxiriga quyidagi ko’rinishda qo’shuvchi dastur tuzing.
"""
import random
randomsonlar =[random.randint(1,100)for i in range (20)]
print (randomsonlar)
a = sum(randomsonlar) 
print