def add_binary(a: str, b: str) -> str:
    i , j = len(a) - 1, len(b) - 1
    ans = ""
    sum = 0
    while i >= 0 or j >= 0:
        x = int(a[i]) if i >= 0 else 0
        y = int(b[j]) if j >= 0 else 0
        sum += x + y
        ans += str(sum % 2)
        sum //= 2
        i -= 1
        j -= 1
    if sum:
        ans += str(sum)
    return ''.join(reversed(ans))

def add_binary_v2(a: str, b: str) -> str:
    a , b = int(a , 2) , int(b , 2)
    return bin(a + b)[2:]

if __name__ == '__main__':
    print(add_binary('110','1'))
    print(add_binary_v2('110','1'))
    # 110
    # 001
    # 111
