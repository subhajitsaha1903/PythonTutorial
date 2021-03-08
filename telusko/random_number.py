# generating a random number
import random

# random will generate random number between 1 and 0
# random_number_value = random.random()
# print(random_number_value)


# uniform will generate random number between the range provided as argument
# random_value = random.uniform(1, 10)
# print(random_value)


# generating random integer within a given range provided
# random_integer_value = random.randint(1, 6)
# print(random_integer_value)


name = ["subhajit", "abhi", "sumana", "surajit", "avijit", "suman"]
random_name = random.choice(name)
print(random_name)
