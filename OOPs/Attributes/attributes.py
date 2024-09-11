class Worker:
    city="Vijayawada"           #class Attributes....
    def __init__(self,name,age):
        self.name=name          #objects  (or) instance Attributes
        self.age=age 
    def dis(self):
        print("The name of the worker is ",self.name," and his age is ",self.age," from city of ",Worker.city,".",sep="")

name=input("Enter the name: ")
age=int(input())
W1=Worker(name,age)
W1.dis()

