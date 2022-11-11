
def factorial(x: int):
    """Function calculates factorial of int number > 0
    """
    if x == 1:
        return 1
    elif x <= 0:
        return None
    else:
        return x * factorial(x - 1)


print(factorial(0))
print(factorial(5))
print(factorial(1))