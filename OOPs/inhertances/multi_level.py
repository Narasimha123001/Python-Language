class Grand:
    def __init__(self,x):
        self.x=x
class Father(Grand):
    def __init__(self,x,y):
        super().__init__(x)
        self.y=y
class Son(Father):
    def __init__(self,x,y,z):
        super().__init__(x,y)
        self.z=z

    def son(self):
        return self.x+self.y+self.z
x,y,z=map(int,input().split())
s1=Son(x,y,z)
print(s1.son())