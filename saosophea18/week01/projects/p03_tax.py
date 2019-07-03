AMOUNT_INTER = 0
RATE = 0
while True:
    print("Please enter your amount:")
    AMOUNT_INTER = input()

    if(not (AMOUNT_INTER.isdigit())):
        print("Number is incorrect, try again.")
    else:
        break
while True:
    print("Please enter tax rate:")
    RATE = input()

    if( (not(RATE.isdigit())) or (not ((int(RATE) >=1) and (int(RATE) <=99))) ):
        print("Rate is incorrect, try again.")
    else:
        break
AMOUNT_INTER = int(AMOUNT_INTER)
RATE = int(RATE)
print("===== ===== ===== ===== =====")
print("AMOUNT: " + str(AMOUNT_INTER))
print("RATE: " + str(RATE) + "%")
print("===== ===== ===== ===== =====")
TAX_AMOUNT = float((RATE/100)*AMOUNT_INTER)
NET = float(AMOUNT_INTER - TAX_AMOUNT)

'{:.2f}'.format(TAX_AMOUNT)
'{:.2f}'.format(NET)

print("TAX: ",TAX_AMOUNT)
print("NET: " + str(NET))
print("===== ===== ===== ===== =====")
