"""
nums = [10, 5, 21, 1, 17]

print("q to exit")
answer = int(input("Please Enter a Number: "))

while(answer != 'q'):
    if(answer == 'q'):
        print("Exiting. . . ")
        break
    elif(answer == nums[3]):
        print("You guessed correctly")
        print("Exiting. . . ")
        break
    else:
        print("You did not guess correctly")
    
    answer = int(input("Please Enter a Number: "))

"""

numbers = [11, 32, 33, 15, 1]

answer = input("Guess a number or type q to quit.")

while (answer != 'q'):

    if answer == "q":
        break
    try:
        answer = int(answer)
    except ValueError:
        print("please type a number or q to quit.")
    if answer in numbers:
        print("You guessed correctly!")
        break
    else:
        print("You guessed incorrectly!")
    
    answer = input("Guess a number or type q to quit.")
