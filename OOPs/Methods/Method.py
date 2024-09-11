class Worker:
    city="Vijayawada"
    def __init__(self,name,age):    
        self.name=name
        self.age= age
    @staticmethod                    #static method : we don't want the self parameter .because they are not bound to -
    def Welocome():                                  # -a particular instance of the class.its worker to evey class
        print("Welcome to my company")
    def dis(self):              #instance method
        print("The name of worker is ",self.name," and his age is ",self.age," is belongs to ",Worker.city,".",sep="")

name=input("Enter your name: ")
age=int(input("Enter yout age: "))
W1=Worker(name,age)
W1.dis()
W1.Welocome()
Worker.Welocome()
"""
or can use Worker.Welocome()
Instance methods can access and modify instance attributes and can also access class attributes if needed. 
They are called on instances of the class and can perform operations specific to each instance.
 """


