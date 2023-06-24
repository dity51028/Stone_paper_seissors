class student:
    def printdetails(self):
        return f"Name is {self.name}. In department {self.dept} of roll no.{self.roll}"

a=student()
a.name="Dipannita"
a.roll=14
a.dept="CSE"
print(a.printdetails())