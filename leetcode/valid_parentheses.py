def is_valid(s: str) -> bool:
    stack = []
    opening_parentheses = '<[{('
    paired = [('(' , ')')  , ('{' , '}') , ('[' , ']') , ('<' , '>')]
    is_empty = lambda stk: len(stk) == 0
    is_paired = lambda p: p in paired
    for c in s:
        if c in opening_parentheses:
            stack.append(c)
        else:
            if is_empty(stack) or not is_paired((stack.pop() , c)):
                return False
    return is_empty(stack)

if __name__ == '__main__':
    x = '<{(<()>{}<>[])}>' #True
    y = '{(<()>{}<>[])}>' #False
    print(is_valid(x))
    print(is_valid(y))
