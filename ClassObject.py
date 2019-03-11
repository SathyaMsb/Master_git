

class Person():
    def name(self):
        print("My name is SathyaMsb")
    def age(self):
        print("My age is 27")

name1 = Person()
age1 = Person()
print("This is one method to call the fun")
Person.name(name1)
Person.age(age1)

print()

print("This is another method to call the fun. Mostly used this fun call")
name1.name()
age1.age()