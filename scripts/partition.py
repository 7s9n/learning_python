from typing import (
    Callable,
    Any,
    Iterable,
    Tuple,
    List,
)
def partition(predicate: Callable, values: Iterable[Any])-> Tuple[List[Any], List[Any]]:
    """
    Split the values into two sets, based on the return value of the function
    (True/False). e.g.:

        >>> partition(lambda x: x > 3, range(5))
        [0, 1, 2, 3], [4]
    """
    results = ([], [])
    for item in values:
        results[predicate(item)].append(item)
    return results

if __name__ == '__main__':
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    even_nums, odd_nums = partition(lambda x: x & 1, nums)

    print(even_nums)
    print(odd_nums)
