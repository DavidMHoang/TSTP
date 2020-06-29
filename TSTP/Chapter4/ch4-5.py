def convert(str):
    """
    Function that converts a string to a float
    :param str: str.
    :return: float of str
    """
    try:
        return float(str)
    except(ValueError):
        print("Invalid Input")

def main():
    result1 = convert("120.0")

    print(result1)

main()
