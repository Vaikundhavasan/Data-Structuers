def semesterMarks(x):
    return (int ( (x/100*80) ) )

def internalMarks(x):
    return (int ( (x/100*20) ) )

def finalMarks(x,y):
    return (semesterMarks(x)+internalMarks(y))

def Result(sm,result):
    if(sm>=45):
        if(result>=50):
            print("\n\t\t\t Result : Pass")
            print("\n\t\t\t Total Mark : " + str(result) )
        else:
            print("\n\t\t\t Result : Fail")
            print("\n\t\t\t Total Mark : " + str(result) )
    else:
        print("\n\t\t\t Result : Fail")
        print("\n\t\t\t Total Mark : " + str(result) )
            
def Revaluation(sm,result):
    if(sm>=45):
        if(result>=50):
            print("\n\t\t\t Result : Pass")
            print("\n\t\t\t Total Mark : " + str(result) )
        else:
            print("\n\t\t\t Result : Fail")
            print("\n\t\t\t Because your Total Mark is less than 50")
            print("\n\t\t\t Your Total Mark : " + str(result) )
    else:
        print("\n\t\t\t Result : Fail")
        print("\n\t\t\t Because your Semester Mark is less than 45")
        print("\n\t\t\t Your Semester Mark : " + str(sm) )
def wrongInput():
    print("\n\t\t\t Wrong Input!")

print("Implement Program Using Function")

sm = int(input("\nEnter Your Semester Marks for 100 : "))
im = int(input("\nEnter Your Internal Marks for 100 : "))


result = finalMarks(sm,im)

ch=1

while(ch==1):
    
    choice = int(input("\n 1. Result \n 2. Revaluation \n 3. Exit \n\n Enter Your Choice : "))
    
    if(choice==1):
        Result(sm,result)
            
    elif(choice==2):
        Revaluation(sm,result)
            
    elif(choice==3):
        ch=0
        
    else:
        wrongInput()
        
