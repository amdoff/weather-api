"""
Foydalanuvchi `int` tipida bitta butun son kiritadi. Bu son burchak gradusini ifodalashini bilsak, 
shu burchak tipini aniqlovchi dastur tuzing. Shartlar:

1. Kiritilgan son 180ga teng bo'lsa ⇒ `YOYIQ BURCHAK`
2. Kiritilgan son 90ga teng bo'lsa ⇒ `TO'G'RI BURCHAK`
3. Kiritilgan son 90 dan kichik bo'lsa ⇒ `O'TKIR BURCHAK`
4. Kiritilgan son 90 dan katta 180 dan kichik bo’lsa ⇒ `O'TMAS BURCHAK`
"""

a = int(input("bitta son kiriting:"))
if a == 180:
    print("Yoyiq burchak")
elif a == 90:
    print("Tog'ri burchak")
elif a < 90:
    print ("O'tkir burchak")
elif a > 90 and a < 180:
    print("O'tmas burchak")
else:
    print("noto'g'ri qiymat")
