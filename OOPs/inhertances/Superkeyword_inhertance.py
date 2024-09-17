class A:
    def funt1(self):
        print("I am Func1")
class B(A):
    def funt1(self):
        print("I am Func1 from class b")
        super().funt1()   # use super class For access parent function ,when they have same function names 
    def funt2(self):
        print("I am Func2")

obj1=B()
obj1.funt1()
