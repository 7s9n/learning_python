
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

    #instance method
    def code(self):
        print(f"{self.name} is writing code...")

    def code_in_language(self , language):
        print(f"{self.name} is writing code in {language}...")

    # def information(self):
    #     information = f"name = {self.name} , age = {self.age} , level = {self.level}"
    #     return information

    #dunder method
    def __str__(self):
        information = f"name = {self.name} , age = {self.age} , level = {self.level}"
        return information

    def __eq__(self , other):
        return self.name == other.name and self.age == other.age

    @staticmethod
    def entry_salary(age):
        if age < 25:
            return 5000
        elif age < 30:
            return 7000
        return 9000
#instance
se1 = SoftwareEngineer('Hussein' , 22 , 'Junior' , 6000)
se2 = SoftwareEngineer('Lisa' , 22 , 'Senior' , 8000)
se3 = SoftwareEngineer('Lisa' , 22 , 'Senior' , 8000)

se1.code()
se2.code()

se1.code_in_language('Python')
se2.code_in_language('C++')

# print(se1.information())

print(se1)
print(se1.__str__())

print(se2 == se3)
print(se2 == se1)

print(se1.entry_salary(24)) #staticmethod decorator must be used otherwise will raise an error
print(SoftwareEngineer.entry_salary(24)) #Ok

#Recap
#instance method(self)
#arguments and can return values
#special "dunder" method (__str__ and __eq__)
#@staticmethod
