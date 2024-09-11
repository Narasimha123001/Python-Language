"""
    1:Constructor are generally used for instantiating values for an obj.
    2:it is defined to initalize the data members of an object when it is created.
    3: in python the ( __init__() ) method is called as construtor and is always called when is object is created.
    """

class Worker:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display(self):
        print("The name of Worker is ",self.name," and the age is ",self.age,".",sep="")

name=input()
age=int(input())
obj1=Worker(name,age)
obj1.display()