#multiple variable/attributes combines and wrap in a single unit is calles encapsulation
class A:
    def __init__(self):
        self.name="name"
    @classmethod
    def show(cls,age):
        cls.age=age
    @staticmethod
    def display(school):
        print(school)

'''access specifier:
          1) public - (govt place)  x=10
          2) protected  (covered campus)  _x=10  (_)
          3) private    (private-house)   __x=10  (__)
          '''

#2) -----------               protected     -------------------------- 
# class A:
#     _x=10    #protected variable
#     def _show(self):   #protected method
#         print("form class A")
# class B(A):
#     pass       #the pass statement is a placeholder that is used when a block of code is syntactically required but you don't want to execute any action
# # there is access of dir
# #print(dir(B))
# class C:
#     pass
# print(dir(C))
# #it doesn't access


#-------------      tread  -----------------
class A:
    __x=10    
    def __show(self):   
        print("form class A")
class B(A):
    pass 
print(dir(B))    
obj=B()
print(obj._A__x)
obj._A__show()  # it give answer
print(obj._A__show())  #it give answer with one None

