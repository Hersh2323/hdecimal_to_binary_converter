# The goal of this application is to convert integer decimal value into binary with a max value of 1024
import random
value_min = 0
value_max = 1024
random_int = random.randint(value_min, value_max)
print('random_int: ' + str(random_int))
binary_result = format(random_int, 'b')
print('Integer converted to binary: ' + binary_result)
