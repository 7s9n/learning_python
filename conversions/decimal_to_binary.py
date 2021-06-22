"""Convert a Decimal Number to a Binary Number."""

def decimal_to_binary(decimal: int) -> str:
    rem , bin , c = 0 , 0 , 0
    is_negative = '-' if decimal < 0 else ''
    decimal = abs(decimal)
    while decimal > 0:
        rem = decimal % 2
        bin += rem * pow(10 , c)
        c += 1
        decimal //= 2
    return f'{is_negative}0b{bin}'

def decimal_to_binary_v2(decimal: int) ->str:
    if not isinstance(decimal , int):
        raise TypeError("You must enter integer value")
    if decimal == 0:
        return '0b0'

    is_negative = False
    if decimal < 0:
        is_negative = True
        decimal = -decimal
    binary: list[int] = []

    while decimal > 0:
        binary.insert(0 , decimal % 2)
        decimal >>= 1 # or num //= 2

    if is_negative:
        return '-0b' + ''.join( str(n) for n in binary )
    else:
        return '0b' + ''.join( str(n) for n in binary )

def binary_recursive(decimal: int) ->str:
    if decimal in (0 , 1):
        return str(decimal)
    div , mod = divmod(decimal , 2)
    return binary_recursive(div) + str(mod)

if __name__ == '__main__':
    print( decimal_to_binary(-900) )
    print( binary_recursive(900) )
    print( decimal_to_binary_v2(-900) )
