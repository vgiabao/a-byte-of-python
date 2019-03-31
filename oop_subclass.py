class SchoolMember:
    ''' represents any school member'''
    def __init__(self, name , age):
        self.name = name
        self.age = age
        print('initialize SchoolMember: {}'.format(self.name))
    def tell(self):
        print('name: {}, age: {}'.format(self.name, self.age))
class Teacher(SchoolMember):
    def __init__(self, name, age, salary):
        SchoolMember.__init__(self, name, age)
        self.salary = salary
        print('initialize Teacher: {}'.format(self.name))

    def tell(self):
        SchoolMember.tell(self)
        print('Salary: {:d}'.format(self.salary))

class Student(SchoolMember):
    def __init__(self, name, age, marks):
        SchoolMember.__init__(self, name, age)
        self.marks = marks
        print('initialize Student: {}'.format(self.name))
    def tell(self):
        SchoolMember.tell(self)
        print('Marks: {:d}'.format(self.marks))

t = Teacher('Mrs. Shrivi', 40, 1200)
s = Student('bao', 18, 10000000)
members = t,s
for member in members:
    member.tell()
