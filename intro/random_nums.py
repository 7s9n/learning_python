import random as rand


# for _ in range (200):
#     x = rand.randint(1 , 10)
#     assert (1 <= x <= 10)
#     print(x)

x = rand.randrange(1 , 10) # 10 is not included
print(x)

nums = [i for i in range(20)]

random_choice = rand.choice(nums)

print(random_choice)

random_choices = rand.choices(nums , k=3)
print(random_choices)

random_choices = rand.sample(nums , k=3)
print(random_choices)

print(nums) #[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
rand.shuffle(nums)
print(nums)