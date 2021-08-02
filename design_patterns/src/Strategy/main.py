"""
Strategy Design Pattern
In computer programming,
the strategy pattern is a behavioral software design pattern that enables selecting an algorithm
at runtime. Instead of implementing a single algorithm directly,
code receives run-time instructions as to which in a family of algorithms to use.

Typically,
the strategy pattern stores a reference to some code in a data structure,
and retrieves it. This can be achieved by mechanisms such as the native function pointer,
the first-class function, classes or class instances in object-oriented programming languages,
or accessing the language implementation's internal storage of code via reflection.

Source: Wikipedia
"""

from abc import ABCMeta , abstractmethod
from typing import List


class Strategy(metaclass=ABCMeta):
    """
    The Strategy interface declares operations common to all supported
    versions of some algorithm.
    """
    @abstractmethod
    def do_algorithm(self , data: List) -> List:
        pass

"""
Concrete Strategies implement the algorithm while following the base
Strategy interface. The interface makes them interchangeable in the Context.
"""

class SortStrategy(Strategy):
    def do_algorithm(self , data: List) -> List:
        return sorted(data)

class ReverseStrategy(Strategy):
    def do_algorithm(self , data: List) -> List:
        return reversed(data)

class Context:
    def __init__(self , strategy: Strategy):
        """
        Usually, the Context accepts a strategy through the constructor, but
        also provides a setter to change it at runtime.
        """
        self._strategy = strategy

    @property
    def strategy(self) -> Strategy:
        """
        The Context maintains a reference to one of the Strategy objects.
        The Context does not know the concrete class of a strategy. It should
        work with all strategies via the Strategy interface.
        """
        return self._strategy

    @strategy.setter
    def strategy(self , strategy: Strategy) ->None:
        """
        Usually, the Context allows replacing a Strategy object at runtime.
        """
        self._strategy = strategy

    def do_some_logic(self) ->None:
        """
        The Context delegates some work to the Strategy object instead of
        implementing multiple versions of the algorithm on its own.
        """
        result = self.strategy.do_algorithm( ['a' , 'b' , 'c' , 'd'] )
        print( ','.join(result) )

if __name__ == '__main__':
    context = Context(SortStrategy())

    context.do_some_logic()
    context.strategy = ReverseStrategy()
    context.do_some_logic()
