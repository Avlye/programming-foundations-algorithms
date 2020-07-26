def power(number, powerby):
    if powerby == 0:
        return 1
    else:
        return number * power(number, powerby - 1)


def factorial(number):
    if number == 0:
        return 1
    else:
        return factorial(number - 1)


def efun(number):
    if number == 0:
        return 1
    else:
        return number * efun(number - 2)


print("12 power by 2 is {}".format(power(12, 2)))
print("Factorial of 12 is {}".format(factorial(12)))
print("Efun of 8 is {}".format(efun(8)))