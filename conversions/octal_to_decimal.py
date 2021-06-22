def octal_to_decimal(octal: str) -> int:
    if not octal:
        raise ValueError("Empty string was passed to the function")

    is_negative = octal[0] == '-'
    if is_negative:
        octal = octal[1:]

    if not octal.isdigit() or not all(0 <= int(d) <= 7 for d in octal):
        raise ValueError("Non-octal value was passed to the function")

    decimal = 0
    for digit in octal:
        decimal = 8 * decimal + int(digit)
    if is_negative:
        decimal = -decimal
    return decimal


def octal_to_decimal_v2(octal: str) -> int:
    if not octal:
        raise ValueError("Empty string was passed to the function")

    is_negative = octal[0] == '-'
    if is_negative:
        octal = octal[1:]

    if not octal.isdigit() or not all(0 <= int(d) <= 7 for d in octal):
        raise ValueError("Non-octal value was passed to the function")

    decimal , c = 0 , 0
    for digit in octal[::-1]:
        decimal += int(digit) * pow(8 , c)
        c += 1
    if is_negative:
        decimal = -decimal
    return decimal
if __name__ == '__main__':
    print(int(-0o77777))
    print( octal_to_decimal('-77777') )

    print(int(0o7445777))
    print( octal_to_decimal('7445777') )

    print(int(-0o45475777))
    print( octal_to_decimal_v2('-45475777') )
