import random 
a = [ (random.randint(1,50))for i in range (20)]
b = [ (random.randint(1,50))for i in range (20)]
c = list(set(a) ^ set(b))

print(a)
print(b)
print(c)