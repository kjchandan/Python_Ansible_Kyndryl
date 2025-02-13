# class Infant:
#     pass

# baby=Infant()
# help(Infant) #Help on class Chandan in module __main__:
# help(baby)    #Help on Chandan in module __main__ object:

# -------------------------------------------------------------------

class Mom:
    def __del__(self): #Destrcutor - Once the object is exceuted then later the destrcutor is executed
          print("Object destroyed")

    def walk(self):  #self -> Placeholder which holds the object - Standard first paramter to the method of the class(1st paramter to the method of class is object to the class.)
        print("Walk - Mom", id(self))

    def __init__(self):
        print("Object constructed successfully")

class Infant(Mom):
     def walk(self):
          print("Walk Infant")

baby= Infant()
baby.walk()

# mother=Mom()    
# mother.walk()   #Current Object
# print("id(mother)",id(mother)) # id() -> If same number appears in the output means it belongs to Same object.
# Mom.walk(mother)

# del mother
# print("THis will be displayed last")



# ----------------------------------------------------------------------
# -------------------Constructor---------------

