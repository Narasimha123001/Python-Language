#parentclass
class Parent:
    def __init__(self,x,y):
        self.x=x
        self.y=y
#child 1(add)
class Child1(Parent):
 
    def child1(self):
        return self.x+self.y
#child 2(sub)
class Child2(Parent):

    def child2(self):
        return self.x-self.y    
#child 3(Mul)  
class Child3(Parent):
    
    def child3(self):
        return self.x*self.y

x,y=map(int,input().split())
C1=Child1(x,y)
C2=Child2(x,y)
C3=Child3(x,y)

print(C1.child1())
print(C2.child2())
print(C3.child3())