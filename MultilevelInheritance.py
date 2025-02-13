#//Multilevel Inheritance 

class MGM:
    def walk3(self):    #3 (MGM) - after MGM in Mom class the MGF class is called.
        print("Walk MGM")
class MGF:
    def walk4(self):    #4(MGF) - after MGF in Mom class then later there is no class, then it goes to next class Dad.
        print("Walk MGF") 
class PGM:              #6(PGM) -  After PGM class it goes to the PGF class which is in the Dad class 2nd method i.ie,Dad(PGM.PGF)
    def walk6(self): 
        print("Walk PGM")
class PGF:
     def walk7(self):   #7(PGF) - is called at last
          print("Walk PGF")
class Mom(MGM,MGF):     #2 (Mom) - here the MGM class is first called- soo it the later calls MGM class.
     def walk2(self):
          print("Walk Mom")
class Dad(PGM, PGF):    #5 (Dad) - After dad class , inside the dad there is PGM class , it goes to PGM class.
     def walk5(self):
          print("Walk Dad")
class Infant(Mom,Dad):  #1 - In Infant there is Mom class first (then Mom gets called)
     def walk1(self):
          print("Walk Infant")

baby= Infant()          #0 - Infant is called
baby.walk()