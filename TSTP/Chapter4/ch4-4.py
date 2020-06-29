def func1(x):
    """
    Function that divides the parameter by 2.
    :param x: int.
    :return: x divided by 2.
    """
    return x / 2

def func2(x):
    """
    Function that multiplies the parameter by 4.
    :param x: int.
    :return: x times 4
    """
    return x * 4

def main():
    var1 = func1(6)
    var2 = func2(var1)

    print(var1)
    print(var2)

main()
