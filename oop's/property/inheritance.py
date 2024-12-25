# -------------------              single level               ------------------------
# class p:
#     def __init__(self,p_name):
#         self.x=p_name
#     def p_properties(self,home,bank):
#         self.h=home
#         self.b=bank
# class c(p):
#     def c_property(self,quali):
#         self.q=quali
#         print(self.h)
#         print(self.b)
#         print(self.q)
#         print(self.x)
# obj=c("twinkle")
# obj.p_properties("bhopal","HDFC")
# obj.c_property("B.Tech")

# -----------------------           multi level           --------------------------------
# class gf:
#     def name(self,name):
#         self.name=name
# class p(gf):
#     def __init__(self,p_name):
#         self.x=p_name
#     def p_properties(self,home,bank):
#         self.h=home
#         self.b=bank
# class c(p):
#     def c_property(self,quali):
#         self.q=quali
#         self.p_properties("bhopal","hdfc")
#         # print(self.h)
#         print(self.b)
#         # print(self.q)
#         print(self.x)
# obj=c("twinkle")
# # obj.p_properties("bhopal","HDFC")
# obj.c_property("B.Tech")

# class Gf:
#     def name(self,name):
#         self.x=name
#         print(self.x)
# class F(Gf):
#     def f_name(self,f_name):
#         self.y=f_name
# class C(F):
#     def c_name(self,c_name):
#         self.z=c_name
# obj=C()
# obj.name("twinkle")

#-----------------------------            multiple inheritance      ----------------------
class father:
    x=10
    y=20
    def property(self,f_name,f_bank):
        self.name=f_name
        self.bank=f_bank
        print(self.name)
        print(self.bank)
class mother:
    a=10
    b=20
    def property1(self,m_name,m_bank):
        self.name1=m_name
        self.bank1=m_bank
        print(self.name1)
        print(self.bank1)
class son(father,mother):
    pass
# print(dir(son))
obj=son()
obj.property1("twinkle","HDFC")
obj.property("thakre","icici")


#-------------------------           hybrid inheritance             -----------------------
class A:
    def __init__(self,p_name):
        self.x=p_name
    def property(self,home,bank):
        self.h=home
        self.b=bank
class B(A):
    pass

