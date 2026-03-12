class PersonalInfo:
    def __init__(self, name, dob, phone, email):
        self.name = name
        self.dob = dob
        self.phone = phone
        self.email = email

    def display_personal(self):
        print("Name:", self.name)
        print("DOB:", self.dob)
        print("Phone:", self.phone)
        print("Email:", self.email)


class Education(PersonalInfo):
    def __init__(self, name, dob, phone, email, degree, university, year, cgpa):
        super().__init__(name, dob, phone, email)
        self.degree = degree
        self.university = university
        self.year = year
        self.cgpa = cgpa

    def display_education(self):
        print("Degree:", self.degree)
        print("University:", self.university)
        print("Year:", self.year)
        print("CGPA:", self.cgpa)


class Experience(Education):
    def __init__(self, name, dob, phone, email, degree, university, year, cgpa,
                 company, role, years, skills):
        super().__init__(name, dob, phone, email, degree, university, year, cgpa)
        self.company = company
        self.role = role
        self.years = years
        self.skills = skills

    def display_experience(self):
        print("Company:", self.company)
        print("Role:", self.role)
        print("Experience:", self.years)
        print("Skills:", self.skills)

class CandidateProfile(Experience):
    def display_profile(self):
        self.display_personal()
        self.display_education()
        self.display_experience()

        if self.years > 5:
            print("Eligible for Senior Role")
        else:
            print("Eligible for Junior Role")

        print("----------------------")

c1 = CandidateProfile("Rahul", "10-05-1998", "9876543210",
                      "rahul@gmail.com",
                      "B.Tech", "ANITS", 2020, 8.5,
                      "Infosys", "Developer", 6, "Python, SQL")

c2 = CandidateProfile("Srinu", "15-07-2001", "9876549999",
                      "srinu@gmail.com",
                      "B.Tech", "AU", 2023, 8.8,
                      "TCS", "Engineer", 2, "Java, Web")

c1.display_profile()
c2.display_profile()



'''
Name: Rahul
DOB: 10-05-1998
Phone: 9876543210
Email: rahul@gmail.com
Degree: B.Tech
University: ANITS
Year: 2020
CGPA: 8.5
Company: Infosys
Role: Developer
Experience: 6
Skills: Python, SQL
Eligible for Senior Role
----------------------
Name: Srinu
DOB: 15-07-2001
Phone: 9876549999
Email: srinu@gmail.com
Degree: B.Tech
University: AU
Year: 2023
CGPA: 8.8
Company: TCS
Role: Engineer
Experience: 2
Skills: Java, Web
Eligible for Junior Role
----------------------

'''
