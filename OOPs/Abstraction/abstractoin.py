from abc import ABC ,abstractmethod

class Polygon(ABC):
    @abstractmethod
    def noofsides(self):
        pass

class Triangle(Polygon):
    def noofsides(self):
        print("I have 3 sides...")
class Pentagon(Polygon):
    def noofsides(self):
        print("I have 5 sides...")
class Hexagon(Polygon):
    def noofsides(self):
        print("I have 6 sides....")
class Quadrilateral(Polygon):
    def noofsides(self):
        print("I have 7 sides....")

C1=Triangle()
C1.noofsides()
C2=Pentagon()
C2.noofsides()
C3=Hexagon()
C3.noofsides()
C4=Quadrilateral()
C4.noofsides()