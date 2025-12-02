import random 
a = {random.randint(1,100) for i in range(10)}
b = {random.randint(1,100) for i in range (10)}
c = a.intersection(b)
d = sum (c)

print(a)
print(b)
print(c)
print("yigindi",d)

