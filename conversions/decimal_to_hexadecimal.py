def decimal_to_hexadecimal(decimal: int)-> str:
    """Convert a Decimal Number to a Hexadecimal Number."""
    if not isinstance(decimal , int):
        raise TypeError("You must enter integer value")
    if decimal == 0:
        return '0x0'
    is_negative = '-' if decimal < 0 else ''
    decimal = abs(decimal)
    chars = '0123456789abcdef'
    hex: list[str] = []
    while decimal > 0:
        hex.insert(0 , chars[decimal % 16])
        decimal //= 16
    return f'{is_negative}0x{"".join(hex)}'

if __name__ == '__main__':
    print(hex(-100))
    print(decimal_to_hexadecimal(-100))
    
    for i in range(1 , 100000):
        print(decimal_to_hexadecimal(i))
        print(hex(i))
        assert decimal_to_hexadecimal(i) == hex(i)

    for i in range(1 , -100000 , -1):
        print(decimal_to_hexadecimal(i))
        print(hex(i))
        assert decimal_to_hexadecimal(i) == hex(i)
