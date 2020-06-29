answer = input("Do you like chicken?: ")

with open("answer.txt", "w") as f:
    f.write(answer)

with open("answer.txt", "r") as f:
    print(f.read())
