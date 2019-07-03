print("Enter your secret message:")
str = ""
input1 = input()
if(input1==""):
    print("Nothing to encode.")
else:
    for i in range(0,len(input1)):
        if(ord(input1[i])>=97 and ord(input1[i])<=109):
            str += chr(ord(input1[i])+13)
        elif(ord(input1[i])>=110 and ord(input1[i])<=122):
            str += chr(ord(input1[i])-13)
        elif(ord(input1[i])>=65 and ord(input1[i])<=77):
            str += chr(ord(input1[i])+13)
        elif(ord(input1[i])>=78 and ord(input1[i])<=90):
            str += chr(ord(input1[i])-13)
        else:
            str += input1[i]
    print(str)