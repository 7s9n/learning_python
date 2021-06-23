class Employee:
    """This class represents employees in a company """
    num_of_employees = 0 #public static attribute

    # init method or constructor
    def __init__(self , first , last , pay):
        self._first = first #protected Attribute
        self._last = last #protected Attribute
        self._pay = pay

        Employee.num_of_employees += 1

    @property
    def full_name(self)-> str:
        return f'{self._first} {self._last}'

    @property
    def first(self)->str:
        return self._first
    @property
    def last(self)->str:
        return self._last
    @property
    def pay(self)-> int:
        return self._pay

    @property
    def email(self):
        return f'{self.first}.{self.last}@gmail.com'

    def __str__(self):
        return f'Full Name: {self.full_name}.\
        \nPayment: {self.pay}.\
        \nEmail: {self.email}'

    def __repr__(self):
        return f"Employee('{self.first}' , '{self.last}' , {self.pay})"
    #Additional constructor
    @classmethod
    def from_string(cls , str , delimiter = '-'):
        first , last , pay = str.split(delimiter)
        return cls(first , last , pay)

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True


if __name__ == '__main__':
    hussein = Employee('Hussein' , 'Sarea' , 15000)
    print(hussein)

    moataz = Employee.from_string('Moataz-Sarea-20000')
    print(moataz)

    #import datetime

    #date = datetime.date(2021 , 6 , 23)

    #print(Employee.is_workday(date))

    #print(hussein.get_full_name())

    print(hussein.__repr__()) #Employee('Hussein' , 'Sarea' , 15000)
