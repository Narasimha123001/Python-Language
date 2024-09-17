class Father:
    def __init__(self,x):
        self.x=x

class Mother:
    def __init__(self,y):
        self.y=y

class Son(Father,Mother):
    def __init__(self,x,y):
        Father.__init__(self,x)
        Mother.__init__(self,y)
    def son(self):
        return self.x+self.y
x,y=map(int,input().split())
S1=Son(x,y)
print(S1.son())