

while True:
    print("Enter a number:")
    input1 = str(input())
    try:
        if (int(input1) % 2 == 0):
            print(input1 + " is EVEN")

        elif (int(input1) % 2 != 0):
            print(input1 + " is ODD")
    except ValueError:
        if (input1 == "EXIT" or input1 == "exit"):
            exit()
        elif (input is not int):
            print(input1 + " is not a valid number.")
