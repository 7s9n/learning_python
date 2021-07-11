
class SoftwareEngineer:
    def __init__(self):
        self._salary = None #protected attribute
    #getter
    @property
    def salary(self):
        #checks , constraints , calculations
        return self._salary

    #setter
    @salary.setter
    def salary(self , value):
        self._salary = value

    #deleter
    @salary.deleter
    def salary(self):
        # self.salary = None
        del self._salary #or self._salary = None

se = SoftwareEngineer()
se.salary = 6000
print( se.salary )
del se.salary
print(se.salary)

#Recap
#encapsulation
#abstraction
#public ( fun() , value ), protected ( _fun() , _value ), and private( __fun() , __value )
#getter / setter
#getter -> property
#setter -> x.setter
#deleter -> x.deleter