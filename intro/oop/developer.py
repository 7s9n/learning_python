from employee import Employee
class Developer(Employee):
    def __init__(self , first , last , pay , prog_lang):
        Employee.__init__(self , first , last , pay)
        self.__prog_lang = prog_lang

    @property
    def programming_lang(self):
        return self.__prog_lang

    @programming_lang.setter
    def programming_lang(self , lang):
        if isinstance(lang , str):
            self.__prog_lang = lang
        else:
            raise TypeError('Please , enter string')

    def __str__(self):
        str = Employee.__str__(self) # or str = super().__str__()
        return f'Developer\'s {str}\nProgramming language: {self.programming_lang}'

    def __repr__(self):
        return f"Developer('{self.first}' , '{self.last}' , {self.pay} , '{self.programming_lang}')"


if __name__ == '__main__':
    dev_1 = Developer('Hussein' , 'Sarea' , 20000 , 'C++')
    dev_1.programming_lang = 'C++ - Python - Java'
    print(dev_1)

    print( dev_1.__repr__() ) #Developer('Hussein' , 'Sarea' , 20000 , 'C++ - Python - Java')
