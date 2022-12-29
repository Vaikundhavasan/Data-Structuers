def binary(list,n):
    low=0
    high=len(list)-1
    while low<=high:
        mid=(high+low)//2
        mid_value=int(list[mid])
        if(mid_value==n):
            return True
        elif mid_value<n:
            low=mid+1
        elif mid_value>n:
            high=mid-1
list=input("Enter Elements to Create (Seperated by Space) : " ).split() 
print("Entered List : ",list)   
print()
i=1
while(i==1):
    print()
    choice=int(input("'1' for exit Operation , '2' for Perform Operation : " ))
    if(choice==2):
        print()
        n=int(input("Enter a Number to Search : "))
        if(binary(list,n)):
            print("Element Found")
        else:
            print("Element not Found")
            print()
    else:
        i=0
