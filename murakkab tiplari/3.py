text = input("Matnni kiriting: ")
letter = {}

for char in text:
    if char.isalpha(): 
        letter[char] = letter.get(char, 0) + 1
print("Harflar soni:")
for letter, count in letter.items():
    print(f"{letter}: {count}")
