def fcn(obj1, obj2):
    return obj1 is obj2

def main():
    obj1 = input("Please input an object: ")
    obj2 = input("Please input a second object: ")

    print(fcn(obj1, obj2))

main()
