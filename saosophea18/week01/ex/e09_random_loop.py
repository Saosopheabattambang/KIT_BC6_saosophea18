import random
print("Enter a number:")
input = input()
if(input is int):
    for i in range(0,int(input)):
            print(random.randint(1,100))
else:
    print(random.randint(1,100))
