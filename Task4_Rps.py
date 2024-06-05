import random
print("WElcome to game of Rock Paper Scissors 🏮 📄 ✂️)")

print("\n")
options = ("Rock","Paper","Scissors")

continuee = True
count=0

while continuee:
    player = None
    computer = random.choice(options)
    while player not in options:
        player = input("Please Enter Your Choice(Rock  🏮 Paper  📄  Scissors  ✂️  )")
        print("\n")
        if player not in options:
            print(" Please Enter Valid Input Rock,Paper ,Scissors")
    print(f"player: {player}")
    print(f"Computer:   {computer}")


    if player == computer:
        print("It is a Tie 😮")
    elif  player == "Rock" and computer == "Scissors" or player == "Paper" and computer == "Rock" or  player == "Scissors" and computer == "Paper":
        count+=1
        print(f"You win  🏆 and Your Score is  :->  {count}")
    else:
        count-=1
        print("You Lose 🙁")
        print(f"Score is :->    {count}") 
        
          
    playagin = input("play Again ?(y/n): ").lower()
    if not playagin == "y":
        break
    
   
        
        
print("Hope You Enjoy this Game Your Final Score is ",count)
    

