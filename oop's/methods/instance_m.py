class A:
    def new(self):
        print("1st method")  #declaratin
    def new1(self):
        self.new()           # calling
        print("2nd method")
obj=A()
# obj.new()             #calling
obj.new1()            #calling

    