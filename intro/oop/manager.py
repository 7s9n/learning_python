from employee import Employee
from developer import Developer
class Manager(Employee):
    def __init__(self , first , last , pay , employees = None):
        super().__init__(first , last , pay)
        if employees is None:
            self.__employees = []
        else:
            if not all(isinstance(e , Employee) for e in employees):
                raise TypeError('List must only contain  Employee objects')
            self.__employees = employees

    def add_employee(self , employee):
        if not isinstance(employee , Employee):
            raise TypeError('You must add an employee object')
        if employee not in self.__employees:
            self.__employees.append(employee)

    def remove_employee(self , employee):
        if not isinstance(employee , Employee):
            raise TypeError('You must send an employee object to be removed')
        if employee in self.__employees:
            self.__employees.remove(employee)

    def __str__(self):
        str = Employee.__str__(self)
        return f'Manager\'s {str}\nEmployees:\n{"->".join(e.full_name for e in self.__employees)}'

    def __repr__(self):
        return f"Manager('{self.first}' , '{self.last}' , {self.pay} , {self.__employees})"

if __name__ == '__main__':
    dev_1 = Developer('Moataz' , 'Sarea' , 2000 , 'Java')
    dev_2 = Developer('Ahmed' , 'Sarea' , 29900 , 'C')
    dev_3 = Developer('Ekram' , 'Sarea' , 45487 , 'C++')
    manager = Manager('Hussein' , 'Ahmed' , 500000 , [dev_1 , dev_2])
    manager.add_employee(dev_3)

    manager.remove_employee(dev_1)
    print(manager)

    print(manager.__repr__())
