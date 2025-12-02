a = {'key1': 1, 'key2': 3, 'key3': 2}
b = {'key1': 1, 'key2': 2, 'key4': 5}

c = a.keys() & b.keys()  
if c:
    print("O‘xshash kalitlar mavjud:", c)
else:
    print("O‘xshash kalitlar mavjud emas.")
