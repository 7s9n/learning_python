def convertToBase7(num: int)-> str:
    if num == 0:
        return '0'
    ans , n = '' , abs(num)
    while n > 0:
        ans = str(n % 7) + ans
        n //= 7
    return (f'-{ans}' if num < 0 else ans)

print(convertToBase7(-7))