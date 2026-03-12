from datetime import date

class Student:
    def __init__(self, sid, name, marks, dob, fee_paid):
        self.sid = sid
        self.name = name
        self.marks = marks
        self.dob = dob
        self.fee_paid = fee_paid
        self.total_fee = 50000

    def calculate_average(self):
        return sum(self.marks) / len(self.marks)

    def calculate_cgpa(self):
        return self.calculate_average() / 10

    def calculate_age(self):
        today = date.today()
        birth = date(self.dob[2], self.dob[1], self.dob[0])
        age = today.year - birth.year
        return age

    def fee_balance(self):
        return self.total_fee - self.fee_paid

    def display(self):
        print("Student ID:", self.sid)
        print("Name:", self.name)
        print("Marks:", self.marks)
        print("Average:", self.calculate_average())
        print("CGPA:", self.calculate_cgpa())
        print("Age:", self.calculate_age())
        print("Fee Balance:", self.fee_balance())
        print("-----------------------")


class College:
    def __init__(self, code, name, location):
        self.code = code
        self.name = name
        self.location = location
        self.students = []

    def register_student(self, student):
        self.students.append(student)

    def display_details(self):
        print("College Code:", self.code)
        print("College Name:", self.name)
        print("Location:", self.location)
        print("\nStudent Details\n")

        for s in self.students:
            s.display()
c = College("ANITS01", "ANITS", "Visakhapatnam")

s1 = Student(1, "Srinu", [80, 75, 90], (10, 5, 2004), 40000)
s2 = Student(2, "Harsha", [70, 85, 78], (12, 8, 2003), 35000)
s3 = Student(3, "Anil", [88, 92, 84], (25, 3, 2004), 45000)

c.register_student(s1)
c.register_student(s2)
c.register_student(s3)

c.display_details()

'''
Student Details

Student ID: 1
Name: Srinu
Marks: [80, 75, 90]
Average: 81.66666666666667
CGPA: 8.166666666666668
Age: 22
Fee Balance: 10000
-----------------------
Student ID: 2
Name: Harsha
Marks: [70, 85, 78]
Average: 77.66666666666667
CGPA: 7.7666666666666675
Age: 23
Fee Balance: 15000
-----------------------
Student ID: 3
Name: Anil
Marks: [88, 92, 84]
Average: 88.0
CGPA: 8.8
Age: 22
Fee Balance: 5000
-----------------------'''