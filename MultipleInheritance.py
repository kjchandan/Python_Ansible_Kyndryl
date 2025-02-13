#//Multiple Inheritance

class Mom:
    def walk2(self):  #self -> Placeholder which holds the object - Standard first paramter to the method of the class(1st paramter to the method of class is object to the class.)
        print("Walk Mom")
    
class Dad:
     def walk3(self):
          print("Walk Dad")

class Infant(Mom,Dad):
     def walk1(self):
          print("Walk Infant")

baby= Infant()
baby.walk()