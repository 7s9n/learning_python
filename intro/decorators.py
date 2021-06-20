from functools import wraps
# def start_end_decorator(func):
#     def wrapper():
#         print('Start')
#         func()
#         print('End')
#     return wrapper

# @start_end_decorator
# def print_name():
#     print('Hussein Sarea')


# # print_name = start_end_decorator(func=print_name)

# print_name()

# def my_decorator(func):
#     @wraps(func)
#     def wrapper(*args , **kwargs):
#         print('Start')
#         result = func(*args , **kwargs)
#         print('End')
#         return result
#     return wrapper

# @my_decorator
# def add(n: int):
#     return n + n


# print( add(10) )

def repeat(times: int):
    def my_decorator(func):
        @wraps(func)
        def wrapper(*args , **kwargs):
            for _ in range(times):
                result = func(*args , **kwargs)
            return result
        return wrapper
    return my_decorator

@repeat(times=5)
def greet(s: str):
    print(f'Hello {s}.')

greet('Hussein')