from typing import Any

def allEqual(iterator:list[Any]):
    return len( set(iterator) ) == 1

def all_Equal_v2(lst:list[Any]):
    return not lst or lst.count( lst[0] ) == len(lst)

if __name__ == '__main__':
    nums = [1 , 2 , 3 , 4 , 5]
    print( allEqual(nums) )
    print( all_Equal_v2(nums) )
    
    nums = [1 , 1, 1, 1, 1]
    print( allEqual(nums) )
    print( all_Equal_v2(nums) )
