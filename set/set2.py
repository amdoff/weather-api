import random
a = {random.randint(1,100)for i in range(20)}
b = sorted( a , reverse=True)[0]
print(a)
print(b)



