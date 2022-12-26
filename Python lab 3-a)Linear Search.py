def linearSearch(list, x):

    for i in range(0, len(list)):
        if (int(list[i]) == x):
            return i
    return "Not Found"

list = input("Enter Elements seprated by Spaces : ").split()
print("Entered Lists : ",list)
ch=0
while(ch==0):
    choice = int(input("\n1.Search \n2.Exit \n\nEnter Your Choice :  "))
    if(choice==1):
        print()
        x = int(input("Enter a Key to Search : "))
        result = linearSearch(list, x)
        if(result == "Not Found"):
            print("\nElement not found")
        else:
            print("\nElement found at index: ", result)
    elif(choice==2):
            ch=1
    else:
        print("\nPlease Enter correct details!")
