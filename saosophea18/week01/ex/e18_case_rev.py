print("Enter a string:")
str = ""
input = input()
if(input==""):
    print("Empty")
else:
    for i in range(0,len(input)):
        if(input[i]>="a" and input[i]<="z"):
            str+=input[i].upper()
        else:
            str+=input[i].lower()
print(str)
