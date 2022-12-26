"""
Unit <100 = Free
Unit 100 to 200 = 100$
Unit 200 to 500 = 200$
Unit 500 to 1000 = 500$
Unit >= 1000 =  1000$
"""

print("EB bill using Iterative loops")
print(".............................")

name = input("Enter your Name : ")
unit = int(input("Enter how many Unit you Consumed : "))

bill = 0
while(unit>=0):
    if(unit>=1000):
        bill+=1000
    elif(unit>=500):
        bill+=500
    elif(unit>=200):
        bill+=200
    elif(unit>=100):
        bill+=100
    print("Hello Mr/Mrs." + name )
    print("Your Bill : " + str(bill) + "$")
    break
else:
    print("Enter Positive Numbers only!")
