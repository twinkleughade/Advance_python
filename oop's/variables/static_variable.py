
class Student:
    "Student Information"
    school = "SHSC"                         # declaration of static variable in side class but outside of the mehtod.......
    def __init__(self,name,age):
        self.name = name
        self.age = age
        Student.city = "Bhopal"             # declaration of static variable inside constrctor.......
        print("Calling inside of Constructor = ",Student.school)               # calling of static variable.......
    def add_detail(self):
        Student.school_code=101             # declaration of static variable inside instance method.......
        print("Calling inside of instance method = ",Student.school)               # calling of static variable.......
        print("Calling inside of instance method = ",Student.city)                 # calling of static variable.......
    def show_detail(self):
        print(Student.school)
        print(Student.city)
        print(Student.school_code)
        print("Calling inside of instance method = ",Student.principal)
        
obj = Student("twinkle",37)
print("My_City=",Student.city)
print("My_School=",Student.school)
obj.add_detail()
print("School_code=",Student.school_code)
Student.principal = "Indra Bahadur"        # declaration of static variable.......
obj.show_detail()
