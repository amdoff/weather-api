a = int(input("Enter size: "))
b = {f'key{i}': f'value{i}' for i in range(a)}
print(b)