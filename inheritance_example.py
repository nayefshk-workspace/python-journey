#Inheritance Question

class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender


class Student(Person):
    def __init__(self, name, age, gender, grade): #New value which is to be added is called here
        super().__init__(name, age, gender) #to get the inheritance 
        self.grade = grade


s1 = Student("Nayef", 18, "Male", "A")

print(s1.name)
print(s1.age)
print(s1.gender)
print(s1.grade)