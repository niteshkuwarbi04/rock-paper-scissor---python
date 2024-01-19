import random

def gameWin(comp, You):

    if comp == You:
        return None
    
    elif comp == 'rock':
        if You == 'paper':
            return True
        elif You == 'scissor':
            return False 
        
    elif comp == 'paper':
        if You == 'rock':
            return False
        elif You == 'scissor':
            return True 
        
    elif comp == 'scissor':
        if You == 'rock':
            return True
        elif You == 'paper':
            return False 
    

# print("Comp turn : Rock(r) Paper(p) or Scissor(s) ?")
randNo = random.randint(1, 3)
if randNo == 1:
    comp = 'rock'
elif randNo == 2:
    comp = 'paper'
elif randNo == 3:
    comp = 'scissor'

# You= input("Your turn : Rock(r) Paper(p) or Scissor(s) ? \n")
You = input("Choose any one of the three: Rock, Paper or Scissor \t \n")
a = gameWin(comp, You)

print(f"\t Computer : {comp}")
print(f"\t You chose : {You}")

if a == None:
    print("\t The game is a tie.")
elif a:
    print("\t You win!")
else :
    print("\t You lose")
