#inherits , extend , override
class Employee:
    def __init__(self , name , age , salary):
        self.name = name
        self.age = age
        self.salary = salary

    def work(self):
        print( f"{self.name} is working..." )

class SoftwareEngineer(Employee):

    def __init__(self , name , age , salary , level):
        # super().__init__(name , age , salary)
        super(SoftwareEngineer , self).__init__(name , age , salary)
        self.level = level

    def debug(self):
        print( f"{self.name} is debugging..." )

    def work(self):
        print( f"{self.name} is coding..." )
class Designer(Employee):

    def work(self):
        print( f"{self.name} is designing..." )

    def draw(self):
        print( f"{self.name} is drawing..." )

# se = SoftwareEngineer('Hussein' , 22 , 5000 , 'Junior')
# print( se.name , se.age)
# print(se.level)
# se.work()
# se.debug()
#
# d = Designer('Lisa' , 22 , 4000)
# print( d.name , d.age)
# d.work()
# d.draw()


#polymorphism

employees = [
    SoftwareEngineer('Sara' , 22 , 4445 , 'Junior'),
    SoftwareEngineer('Moataz' , 22 , 9000 , 'Senior'),
    Designer('Asmaa' , 20 , 9000)
]



def motivate_employees(employees):
    for employee in employees:
        employee.work()

motivate_employees(employees)

#Recap
#inheritance: ChildClass(BaseClass)
#inherits , extends , overrides
#super().__init__() or super(class , self).__init__()
#polymorphism
