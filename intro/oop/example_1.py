
#class

class SoftwareEngineer:
    #class attribute
    alias = 'Keyboard Magician'

    def __init__(self , name , age , level , salary):
        #instance attributes
        self.name = name
        self.age = age
        self.level = level
        self.salary = salary

#instance
se1 = SoftwareEngineer('Hussein' , 22 , 'Junior' , 6000)

print(se1.name , se1.age)
print(se1.alias)
print(SoftwareEngineer.alias)

se2 = SoftwareEngineer('Lisa' , 22 , 'Senior' , 8000)

print(se2.name , se2.age)
print(se2.alias)

#Recap
#Create class (Blueprint)
#Create an instance (object)
#class vs instance
#instance attributes: defined in __init__(self)
#class attributes
