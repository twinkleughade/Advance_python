# class Calculator:
#     def add(self,*n):
#         sum=0
#         for i in n:
#             sum=sum+i
#         print(sum)
#     def sub(self,*n):
#         sub=0
#         for i in n:
#             sub=sub-i
#         print(sub)/



#  without self
class Calculator:
    def add(*n):
        sum=0
        for i in n:
            sum=sum+i
        print(sum)
    def sub(*n):
        sub=0
        for i in n:
            sub=sub-i
        print(sub)
    def pro(*n):
        pro=1
        for i in n:
            pro=pro*i
        print(pro)

            
