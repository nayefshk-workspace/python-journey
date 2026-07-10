# Create a Student class that counts how many students have been created.

class Student:
    school_name = "Delhi Public School"  
    total_students = 0                 

    def __init__(self, name):
        self.name = name                  
        Student.total_students += 1

s1 = Student("Aman")
s2 = Student("Riya")
s3 = Student("Kabir")
s4 = Student("Nayef")

print(Student.school_name)
print("Total students:", Student.total_students)