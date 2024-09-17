class Father:
    def __init__(self,x,y):
        self.x=x 
        self.y=y
class Work(Father):
    def __init__(self,x,y):
        super().__init__(x,y)
    def work(self):
        return self.x+self.y
class Drive(Father):
    def __init(self,x,y):
        super().__init__(x,y)
    def drive(self):
        return self.x-self.y

class Mother:
    def __init__(self,a,b):
        self.a=a
        self.b=b
class Son(Father,Mother):
    def __init__(self,x,y,a,b):
        Father.__init__(self,x,y)
       
        Mother.__init__(self,a,b)
        
    def son(self):
        return self.x+self.y+self.a+self.b
    
x,y,a,b=map(int,input().split())
Obj1=Work(x,y)
obj2=Drive(x,y)
obj3=Son(x,y,a,b)
print(Obj1.work())
print(obj2.drive())
print(obj3.son())







