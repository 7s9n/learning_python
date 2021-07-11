
class SoftwareEngineer:
    def __init__(self , name , age):
        self.name = name
        self.age = age
        self._salary = None #protected attribute
        self.__num_bugs_solved = 0 #private attribute

    def code(self):
        self.__num_bugs_solved += 1

    #getter
    def get_salary(self):
        return self._salary

    #setter
    def set_salary(self , base_value):
        #Check if value is a valid salary
        #enforce constraints
        self._salary = self._calculate_salary(base_value)
    def _calculate_salary(self , base_value):
        if self.__num_bugs_solved < 10:
            return base_value
        elif self.__num_bugs_solved < 100:
            return base_value * 2
        else:
            return base_value * 3

se = SoftwareEngineer('Hussein' , 22)
print( se.name , se.age )
# print( se._salary ) #Ok
# print( se.__num_bugs_solved ) #Error
for i in range(99):
    se.code()

se.set_salary(20000)
print( se.get_salary() )
