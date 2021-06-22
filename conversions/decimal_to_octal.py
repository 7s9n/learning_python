def decimal_to_octal(decimal: int)->str:
    """Convert a Decimal Number to an Octal Number."""
    if not isinstance(decimal , int):
        raise TypeError("You must enter integer value")
    rem , oct , c = 0 , 0 ,0
    is_negative = '-' if decimal < 0 else ''
    decimal = abs(decimal)
    while decimal > 0:
        rem = decimal % 8
        oct += rem * pow(10 , c)
        c+=1
        decimal //= 8
    return f'{is_negative}0o{oct}'

if __name__ == '__main__':
    for i in range(1 , 9000):
        assert decimal_to_octal(i) == oct(i)

    for i in range(1 , -9000 , -1):
        assert decimal_to_octal(i) == oct(i)
