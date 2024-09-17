class Parent:
    def parent(self):
        print("Father:X")
        print("Father:Y")
class Son(Parent):
    def Print(self):
        print("Son:a")
class Dau(Parent):
    def Print(self):
        print("Dau:b")

obj1=Son()
obj2=Dau()
obj1.Print()
obj1.parent()

print("--")
obj2.Print()
obj2.parent()

