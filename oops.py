class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def rsult(self):
        if self.marks >= 33:
            print(self.name, "passed")
        else:
            print(self.name, "failed")

s1 = Student("akash", 80)
s2 = Student("rahul", 20)

s1.rsult()
s2.rsult()