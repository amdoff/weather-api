class Person:
    def __init__(self, id, ism, familiya, email, oylik):
        self.id = id
        self.ism = ism
        self.familya = familiya
        self.email = email
        self.oylik = oylik

    def __repr__(self):
        return f"Person:(id:{self.id}, ism:{self.ism}, familiya:{self.familya}, email:{self.email}, oylik:{self.oylik})"

people_data = []

persons = []
for data in people_data:
    person = Person(*data)
    persons.append(person)

for person in persons:
    print(person)
