import random

INTRO_MESSAGE = "Welcome to the dice game!"
print(INTRO_MESSAGE)

while True:
    input1 = input("Enter the number of dice you want to roll:")
    sum = 0

    if (input1=="" or not input1.isdigit()):
       print ("USAGE: The number must be between 1 and 8")
       continue

    elif (input1.isdigit()):
        if (int(input1)==1):
            print("TOTAL: " + str(random.randint(1,6)) )
            exit()
        elif(int(input1)>1 and int(input1)<=6):
            for i in range(1,int(input1)+1):
                random1 = random.randint(1,6)
                sum += random1
                print("Dice "+ str(i) + ": " + str(random1))

    print("==========")
    print("TOTAL: " + str(sum))
    print("==========")
    exit()

