
def add_digits(num: int)-> int:
    return 0 if not num else ((num -1) % 9) + 1


if __name__ == '__main__':
    add_digits(38)
