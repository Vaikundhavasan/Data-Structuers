class User:
    def __init__(self,userid,username):
        self.id = userid
        self.name = username
        self.followers = 0
        self.following = 0
        
    def follow(self,user):
        user.followers+=1
        self.following+=1
              
def user_account(x):
    print(x.name,end=" , Followers : " )
    print(x.followers)
    print(x.name,end=" , Following : " )
    print(x.following)

user1 = User("001","Vasan")
user2 = User("002","Vaikundhavasan")
user3 = User("003","Tommy")
user4 = User("004","Charlie")



program_end = False
while(program_end==False):
    user_choice = int(input("\n1.Display My Account \n2.I want to Follow Someone \n3.Exit \n Enter Your Choice : "))
    print()
    if(user_choice==1):
        user_account(user1)
    
    elif(user_choice==2):
        follow_section_end=False
        while(follow_section_end==False):
            choice = int(input(f"Who Want to you follow?\n 1.{user2.name} \n 2.{user3.name} \n 3.{user4.name} \n4.I want Exit Follow Section \n Enter your Choice : "))
            print()
            if(choice==1):
                user1.follow(user2)
            elif(choice==2):
                user1.follow(user2)
            elif(choice==3):
                user1.follow(user2)
            elif(choice==4):
                follow_section_end=True
            else:
                print("Wrong Input!")
    elif(user_choice==3):
        program_end = True
    else:
        print("Wrong Input!")
