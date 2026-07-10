# Create a class Person with a constructor ( __init__ ) that accepts name and age as arguments and stores them as instance attributes.
# Create an object and print the person’s name and age

class Person:
    def __init__(self, name, age, gender):
        self.name = name 
        self.age = age 
        self.gender = gender

p1 = Person("Nayef", 18, "Male")
p2 = Person("Ceaser", 92,"Male")
p3 = Person("Alexzander", 32,"Great")

print(p3.name,p3.gender)



