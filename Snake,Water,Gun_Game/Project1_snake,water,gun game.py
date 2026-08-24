'''
1 for snake 
-1 for water 
0 for gun 
'''
import random
computer = random.choice([0,-1,1])
youstr = input("Enter your choice : ")
youdict = { "s" : 1 , "w" : -1 ,"g" : 0}
you = youdict[youstr]
reversedic = { 1 : 'snake' , -1 : 'water' , 0 : 'gun'}

print(f"You chose {reversedic[you]}\ncomputer chose {reversedic[computer]}")
if (computer == you):
    print("Its a draw")
else:    
    if (computer == -1  and you == 1):
        print("You Win !!!")
    elif(computer == -1  and you == 0):
        print("You Lose!!!")
    elif(computer == 1  and you == -1):
        print("You Lose!!!")
    elif(computer == 1  and you == 0):
        print("You Win!!!")
    elif(computer == 0  and you == -1):
        print("You Win!!!")
    elif(computer == 0  and you == 1):
        print("You Lose!!!")
    else:
        print("Something went wrong")








