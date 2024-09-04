"""
    Class and object: storteing the variable and functions in a contianer called Class and the implemtation of class is called object.
    """

class Person:
    def setValues(self,x,y):
        self.x=x
        self.y=y
    def getValues(self):
        return self.x+self.y

obj1=Person()
#takeing inputs from user
x,y=map(int,input().split())
obj1.setValues(x,y)
print(obj1.getValues())