from linked_stack import LinkedStack

def convert(number: int , radix: int) -> str:
    """
    Convert decimal number to another radix

    Parameters
    -------------
    number: int is the number to be converted.
    radix: int is the radix

    Returns
    --------
    another radix
    """
    if radix < 2 or radix > 32:
        raise ValueError('Radix must be between [2 - 32]')

    def get_char(n: int)->str:
        if 0 <= n <= 9:
            return chr( n + ord('0') )
        else:
            return chr( n - 10 + ord('a') )
    stack: LinkedStack = LinkedStack()

    is_negative = True if number < 0 else False
    number = abs(number)
    while number:
        stack.push( get_char( int(number % radix) ) )
        number //= radix
    if is_negative:
        stack.push('-')
    return ''.join([str(n) for n in stack])


def main():

    print( convert(-121212 , 32) )
    print( convert(282 , 16) )


if __name__ == '__main__':
    main()
