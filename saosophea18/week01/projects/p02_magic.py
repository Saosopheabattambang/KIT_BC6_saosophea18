import random

COUNT = 0
INPUT_Y = 0

QUESTION = "Hello, what is your name?"
print (QUESTION)

INPUT_NAME = input()
print ("Well "+ INPUT_NAME + ", try to guess the number I have in mind!")

while True:
    if( INPUT_Y == 1):
        INPUT_Y = 0
        COUNT = 0
    INPUT_NUMBER = input()

    if(INPUT_NUMBER.isalpha() or INPUT_NUMBER == ""):
        print("Invalid number, USAGE: 1-88, try again!")
    else:
        INPUT_NUMBER = int(INPUT_NUMBER)

        if ( (INPUT_NUMBER <1) or (INPUT_NUMBER > 88) ):
            print ("Invalid number, USAGE: 1-88, try again!")
            continue

        N = random.randint(1,4)

        if ( INPUT_NUMBER != N):
            COUNT = COUNT + 1

            if(INPUT_NUMBER > N):
                print("Too high, try again!")
            elif (INPUT_NUMBER < N ):
                print("Too low, try again!")
            continue

        elif ( INPUT_NUMBER == N):
            COUNT = COUNT + 1
            if ( COUNT == 1):
                print("You won in 1 turn only, that's amazing!")

            elif ( COUNT > 0):
               print("It took you " + str(COUNT) + " turns to guess my number which was " + str(N)+"!")
            while True:
                print("Do you want to play again? [Y/N]")
                INPUT_Y_N = input()
                if (INPUT_Y_N == "N"):
                    print("Ok, bye " + INPUT_NAME + "! See you later!")
                    exit()
                elif ( INPUT_Y_N== "Y"):
                    INPUT_Y = 1
                    break
                else:
                    print("Sorry, I did not understand, Let me repeat:")
                    continue