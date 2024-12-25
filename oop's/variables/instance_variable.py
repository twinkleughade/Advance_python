# class Student:
#     "student information"
#     name='twinkle'
#     age=26
#     def __init__(self):
#         print(id(self))
#         print("Constructor Callled..................")
#     def add(p,q):
#         return p+q
# obj=Student()
# obj2=Student()
# print(id(obj))
# print(id(obj2))
# print(dir(Student))
# print(Student.__doc__)
# print(Student.__dict__)
# obj = Student 
# print(obj.name)
# print(obj.age)
# x=obj.add(5,6)
# print(x)



# class student:
#     "student information"
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#         print(name)
#         print(age)
#         print(self.name)
#         print(self.age)
# obj=student("twinkle",26)
# obj1=student("twi",23)

# class student:
#     "stundent information"
#     def __init__(self,name,age):
#         self.name=name 
#         self.age=age
#     def show_detail(self):
#         print(self.name)
#         print(self.age)
# obj =student("twinkle",26)
# obj.show_detail()

# obj1=student('twi',23)
# obj1.show_detail()



#declaration and calling in instance variable insidde class
class student:
    def __init__(self,name,age):
        self.name=name  #declaration 
        self.age=age    #of instance variable
        print(self.name) #calling
    def add(self,school):
        self.school=school #declaration
    def show_detail(self):
        print(self.name) #calling
        print(self.age)  #calling
        print(self.school) #calling
        print(self.city)
obj =student("twinkle",26)
obj.add('SHSC')
# obj.show_detail()
#calling outside class
print(obj.name)   #calling
print(obj.age)
print(obj.school)
obj.city='bhopal'
obj.show_detail()







