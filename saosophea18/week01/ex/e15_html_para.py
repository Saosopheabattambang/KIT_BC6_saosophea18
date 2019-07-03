list = []
i=0
while True:
    print("Enter a string:")
    list.append(input())
    if(list[i]=="GEN"):
        break
    i=i+1
for j in range(0,i):
    print("<p>"+list[j]+"</p>")
