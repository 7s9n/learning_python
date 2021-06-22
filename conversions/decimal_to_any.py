def decimal_to_any(decimal: int , base: int) -> str:
    """Convert a positive integer to another base as str."""

    if not isinstance(decimal , int):
        raise TypeError("You must enter integer value")
    if not 2 <= base <= 32:
        raise ValueError("base must be between 2 and 36")

    def getChar(num: int):
        """This method produces character value of the input integer and returns it"""
        if 0 <= num <= 9:
            return chr(num + ord('0'))
        else:
            return chr(num - 10 + ord('A'))

    is_negative: bool = True if decimal < 0 else False

    decimal = abs(decimal)

    ans: list[str] = []
    while decimal > 0:
        ans.insert(0 , getChar(decimal % base))
        decimal //= base
    if is_negative:
        ans.insert(0 , '-')

    return ''.join(ans)

if __name__ == '__main__':
    print(decimal_to_any(-25454 , 16))
