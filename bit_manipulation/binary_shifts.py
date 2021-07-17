

def logical_left_shift(n: int , shifted_by: int)-> str:
    """
    Take in 2 positive integers.
    'n' is the integer to be logically left shifted 'shifted_by' times.
    i.e. (number << shifted_by)
    Return the shifted binary representation.
    """

    if n < 0 or shifted_by < 0:
        raise ValueError('The value of both number must be positive')
    binary_number = str( bin(n) )[2:]
    binary_number += '0' * shifted_by

    return '0b' + binary_number

def logical_right_shift(n: int , shifted_by: int)-> str:
    """
    Take in 2 positive integers.
    'n' is the integer to be logically right shifted 'shifted_by' times.
    i.e. (number >> shifted_by)
    Return the shifted binary representation.
    """

    if n < 0 or shifted_by < 0:
        raise ValueError('The value of both number must be positive')

    binary_number = str( bin(n) )[2:]
    if shifted_by >= len(binary_number):
        return '0b0'
    binary_number = binary_number[: len(binary_number) - shifted_by ]

    return '0b' + binary_number

if __name__ == '__main__':
    print( logical_left_shift(2 , 1) )
    print( logical_right_shift(2 , 1) )
