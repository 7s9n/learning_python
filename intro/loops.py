from math import sqrt

#check prime numbers
def is_prime(n: int) -> bool:
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    sqrt_of_n = int(sqrt(n) + 1)
    for i in range(3 , sqrt_of_n , 2):
        if n % i == 0:
            return False
    
    return True

# for i in range(4 , 5000):
#     print(f'is {i} prime ? {is_prime(i)}')

#Loop through the letters in the word "Programming":

# for letter in "Programming":
#     print(letter)

# for i in [1 , 2]:
#     print(i)

#range(start , end , step)

# for i in range(10):
#     print(i) # from 0 to 9

# for i in range(1 , 10):
#     print(i) #from 1 to 9

# for i in range(0 , 100 , 2):
#     print(i) # even numbers

# for i in range(1 , 100 , 2):
#     print(i) #odd numbers


# i = 1
# while i <= 10:
#     print(i)
#     i += 1

# i = 0
# while i <= 10:
#     i += 1
#     if i % 2 == 0:
#         continue
#     else:
#         print(i) # will only print odd numbers

# while True:
#     print('Infinite loop')

# x = [1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9]

# for i in x:
#     print(i)

# i = 0
# while i < x.__len__():
#     print(x[i])
#     i += 1

# i = 0
# x_len = len(x)
# while i < x_len:
#     print(x[i])
#     i += 1

# for i in range(0 , len(x)):
#     print(x[i])

#for loops cannot be empty, but if you for some reason have a for loop with no content, 
# put in the pass statement to avoid getting an error.

# for i in [1 , 2 , 3]:
#     pass

# i = 1
# while i < 10:
#     pass 

# board = [
#     [1 , 2 , 3],
#     [4 , 5 , 6],
#     [7 , 8 , 9]
# ]

# for list in board:
#     for num in list:
#         print(num , ' ' , end = '')
#     print()

x = ['a' , 'b' , 'c' , 'd']

# for idx , char in enumerate(x):
#     print(idx , ' ' , char)

for idx , char in enumerate(x , start=1):
    print(idx , ' ' , char)