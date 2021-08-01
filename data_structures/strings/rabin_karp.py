def hash(word: str , prim_number: int):
    h = sum( [ ord(c) *  ( prim_number ** idx ) for idx , c in enumerate(word) ] )
    return h

def rabin_karp(txt: str , pattern: str , prim_number: int = 101):
    output: list[int] = []
    len_pattern: int = len(pattern)
    len_txt: int = len(txt)
    h_pattern: int = hash( pattern , prim_number)
    h_txt: int = hash( txt[:len_pattern] , prim_number )

    if h_txt == h_pattern:
        output.append( 0 )

    n = len_txt - len_pattern + 1

    for i in range( 1 ,  n ):
        h_txt -= hash( txt[i-1] , prim_number )
        h_txt //= prim_number
        h_txt += hash( txt[i + len_pattern-1] ,
        prim_number) * ( prim_number ** (len_pattern -1) )

        if h_txt == h_pattern:
            #This condition is just to make sure there's no spurious hits
            if txt[i: i + len_pattern] == pattern:
                output.append( i )

    return output

if __name__ == '__main__':
    txt = 'World Hello World'
    pattern = 'World'
    print( rabin_karp(txt , pattern) )
