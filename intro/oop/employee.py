class Employee:
    """This class represents employees in a company """
    def __init__(self , name , age):
        self.__name = name #private Attribute
        self.__age = age #private Attribute

    def __str__(self):
        return f'employee {self.__name} with age {self.age}'


if __name__ == '__main__':
    hussein = Employee('Hussein' , 22)
    print(hussein)
