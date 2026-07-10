class Person:
    def __init__(self, name, roll_number):
        self.name = name
        self.roll_number = roll_number

    def show_basic_info(self):
        print(f"Name        : {self.name}")
        print(f"Roll Number : {self.roll_number}")

class Student(Person):
    def __init__(self, name, roll_number, division, previous_year_marks):
        super().__init__(name, roll_number)
        self.division = division
        self.previous_year_marks = previous_year_marks

    def show_details(self):
        self.show_basic_info()
        print(f"Division    : {self.division}")
        print(f"Prev. Marks : {self.previous_year_marks}")
        print("-" * 30)

students = [
    Student("Aarav Sharma", 101, "A", 88),
    Student("Isha Verma", 102, "B", 75),
    Student("Rohan Mehta", 103, "A", 92),
    Student("Sneha Kulkarni", 104, "C", 68), ]


def search_student():
    keyword = input("\nEnter student name or roll number to search: ").strip()

    found = False
    for student in students:
        if keyword.lower() == student.name.lower() or keyword == str(student.roll_number):
            print("\nStudent Found:")
            student.show_details()
            found = True
            break

    if not found:
        print("No student found with that name/roll number.")

def main():
    print("All Students")
    for student in students:
        student.show_details()

    while True:
        search_student()
        again = input("Search another student?").strip().lower()
        if again != "y":
            break

if __name__ == "__main__":
    main()