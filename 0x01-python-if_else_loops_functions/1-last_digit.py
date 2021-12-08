#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
texto = "Last digit of {:d} is {:d} and is "
absnum = abs(number)
if number % 10 > 5 and number > 0:
    print((texto + "greater than 5").format(number, number % 10))
elif number % 10 == 0:
    print((texto + "0").format(number, number % 10))
elif number % 10 < 6 and number > 0:
    print((texto + "less than 6 and not 0").format(number, number % 10))
elif absnum % 10 and number < 0:
    print((texto + "less than 6 and not 0").format(number, (absnum % 10) * -1))
