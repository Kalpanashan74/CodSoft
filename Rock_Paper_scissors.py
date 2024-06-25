import random
options = ["rock","paper","scissors"]
playing = True
player_Score = 0
Computer_Score = 0
while playing:
    computer = random.choice(options)
    player = input("Choose any options (rock,paper,scissors)").lower()
    print(f"Player :{player}")
    print(f"Computer : {computer}")
    if computer == player:
        print("Its a tie")
    elif(player == "rock" and computer == "scissors"):
        player_Score += 1
        print("You won!\n Your score",player_Score)
    elif(player == "paper" and computer == "rock"):
        player_Score += 1
        print("You won!\n Your score",player_Score)
    elif(player == "scissors" and computer == "paper"):
        player_Score += 1
        print("You won!\n Your score",player_Score)
    else:
        Computer_Score +=1 
        print("You lose \n Computer Scores",Computer_Score)
    if not input("Do you want to play again?(y/n): ")=="y":
        playing = False 
