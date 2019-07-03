import sys
sum=0
print("Enter a number:")
input1 = input()
if(str(input1)=="exit"):
        sys.exit()
if(input1.isdigit()):
    print ("TOTAL: "+input1)
    sum=input1
else:
    print("TOTAL: 0")
    input1=0


while True:
    input2 = input()
    if (str(input2) == "exit"):
        sys.exit()
    elif(input2.isalpha() or input2==""):
        print("TOTAL: "+str(sum))
        input1 =sum
    else:
        sum =str(int(input1)+int(input2))
        print("TOTAL: "+str(sum))
        input1 = int(input1)+int(input2)

