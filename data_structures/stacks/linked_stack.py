from typing import Optional , Any
""" A Stack using a linked list like structure """

class LinkedStack:
    """ Private class Node to represent the linked stack data """
    class __Node:
        def __init__(self , data: Any , next = None) -> None:
            self.data = data
            self.next = next

        def __str__(self) -> str:
            return f'{self.data}'

    def __init__(self) -> None:
        self.__top: Optional[__Node] = None

    def __iter__(self):
        node = self.__top
        while node:
            yield node.data
            node = node.next

    def __len__(self) -> int:
        return len( list( iter(self) ) )

    def __str__(self) ->str:
        return ' -> '.join( [str(item) for item in self] )

    def __contains__(self , value):
        for item in self:
            if item == value:
                return True
        return False
    def is_empty(self) -> bool:
        return self.__top == None

    def push(self , item: Any)-> None:
        self.__top = self.__Node(item , self.__top)

    def pop(self) -> Any:

        if self.is_empty():
            raise IndexError('pop from empty stack')

        data = self.__top.data
        self.__top = self.__top.next

        return data

    def peek(self) ->Any:
        if self.is_empty():
            raise IndexError('peek from empty stack')

        assert self.__top is not None # make sure top isn't empty and is_empty work well or not
        return self.__top.data

    def clear(self) -> None:
        self.__top = None

if __name__ == '__main__':
    s = LinkedStack()
    s.push(1)
    s.push(2)
    s.push(3)
    if 1 in s:
        print('Yes')
    # print(s) 3 -> 2 -> 1
    # ss = iter(s)
    #
    # print(len(s))
    # for i in s:
    #     print(i)

    # print( next(ss) )
    s.pop()
    print(len(s))
