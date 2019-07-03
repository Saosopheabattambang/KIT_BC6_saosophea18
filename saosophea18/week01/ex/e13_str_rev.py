print("Enter a string:")
input1 = input()
res = ""
if(input1==""):
    print("The string is empty.")
else:
    for i in range(0,len(input1)):
        res += input1[len(input1)-i-1]
print(res)