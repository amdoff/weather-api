import random
numbers = [random.randint(1, 100) for _ in range(50)]
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

a = [num for num in numbers if not is_prime(num)]
print("Random sonlar:", numbers)
print("Tub sonlar olib tashlandi:", a)