def func(a, b, c, x=1, y=2):
    """
    Function that adds together all the parameter variables.
    :param a: int.
    :param b: int.
    :param c: int.
    :param x: optional, int.
    :param y: optional, int.
    :return: the sum of all parameters.
    """
    return a + b + c + x + y

result = func(1, 2, 3)
print(result)

result2 = func(1, 3, 6, 9, 13)
print(result2)
