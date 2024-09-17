class A:
    def a(self):
        print("I am A")
class Z:
    def z(self):
        print("I am Z")
class B(A):
    def b(self):
        print("I am B but inhertance by A")
class C(A):
    def b(self):
        print("I am c but inhertance by A")
class D(Z,B):
    def d(self):
        print("I am D but inhertence by both A and B")


# Create an object of class D
obj1 = D()
obj1.a()  # Should print: I am A
obj1.b()  # Should print: I am B but inherited from A
obj1.d()  # Should print: I am D but inherited from both A and B
obj1.z()  # Should print: I am Z