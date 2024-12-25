#type 1. -------------------             method overloading    ----------------
# class A:
#     def add(self,x,y):
#         return x+y
#     def add(self,x,y,z):
#         return x+y+z
# obj=A()
# obj.add(10,20)


#type 2. -------------------             method over-riding    ---------
class A:
    def display(self):
        print("from class A")

class B(A):
    def display(self):
        print("from class B")
    def p(self):
        self.display()
        super().display()  #we can take value of method of parent(super method)
obj=B()
obj.p()
obj.display()

#-----------------         with variable length arguments *  ---------------
# class A:
#     def add(self,*n):
#         sum=0
#         for i in n:
#             sum=sum+i
#         return sum
# obj=A()
# x=obj.add(10,20)
# print(x)
# y=obj.add(10,20,30)
# print(y)
# z=obj.add(10,20,30,40) 
# print(z)      
    