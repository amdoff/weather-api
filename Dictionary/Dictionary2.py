text = input("matini kiriting ")
a = {}
for b in text:
    if b.isalpha():
        a[b] = a.get(b,0)+1
print(a)