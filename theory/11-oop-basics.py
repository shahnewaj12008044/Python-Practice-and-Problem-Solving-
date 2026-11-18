# classes and objects

class Student:
    def __init__(self, name, dept, cgpa):
        self.name = name
        self.dept = dept
        self.cgpa = cgpa

    def show_info(self):
        print(f"{self.name} - {self.dept}, CGPA: {self.cgpa}")

s1 = Student("Shahnewaj", "Physics", 3.52)
s1.show_info()

s2 = Student("Rahim", "Chemistry", 3.80)
s2.show_info()

# inheritance
class ResearchStudent(Student):
    def __init__(self, name, dept, cgpa, topic):
        super().__init__(name, dept, cgpa)
        self.topic = topic

    def show_info(self):
        super().show_info()
        print("Research topic:", self.topic)

r1 = ResearchStudent("Shahnewaj", "Physics", 3.52, "56Fe cross-sections")
r1.show_info()


# Sample output:
# Shahnewaj - Physics, CGPA: 3.52
# Rahim - Chemistry, CGPA: 3.8
# Shahnewaj - Physics, CGPA: 3.52
# Research topic: 56Fe cross-sections
