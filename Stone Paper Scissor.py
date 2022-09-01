import random

def winorloose(comp,user):
    if comp==user:
        print("tied !!!")

    if comp=='s' and user=='o':
        print("You won !!! and comp chose :",comp )
    elif comp=='o' and user=='s':
        print("Comp won !! and comp chose :",comp)
    elif comp =='p' and user=='s':
        print("You won !!! and comp chose :",comp)
    elif comp=='s' and comp=='p':
        print("Comp won !! and comp chose :",comp)
    elif comp =='p' and user=='o':
        print("Comp won !! and comp chose :",comp)
    elif comp =='o' and user=='p':
        print("You won !!! and comp chose :",comp)

        
    
    






def trans(comp,user):
    if comp==1:
        comp='s'
        winorloose(comp,user)
    elif comp==2:
        comp='p'
        winorloose(comp,user)

    elif comp==3:
        winorloose(comp,user)

    
    



print("computer's turn ")
compturn=random.randint(1,3)
userturn=input("your turn \n(s)Scissor \n(p)paper \n(o)stone\n")


if(userturn=='s' or userturn=='p' or userturn=='o'):
    trans(compturn,userturn)
    
else:
    print("enter correct option")

