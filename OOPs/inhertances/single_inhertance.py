class Father:
    def __init__(self,x,y):
        self.x=x
        self.y=y
class Son(Father):
    def son(self):
        Father.__init__(self,x,y)
        return self.x+self.y
    
x,y=map(int,input().split())
s1=Son(x,y)
print(s1.son())
