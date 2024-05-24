print("Rock...")
print("Paper...")
print("Scissors...")

Player1= input("Player 1, Make your move: ")
Player2= input("Player 2, Make your move: ")

if Player1 == "rock" and Player2 == "scissors":
    print("Player1 Wins!")
elif Player1=="rock" and Player2 =="Paper":
    print("Player2 Wins!")
elif Player1=="Paper" and Player2 =="rock":
    print("Player1 Wins!")
elif Player1=="Paper" and Player2 =="scissors":
    print("Player2 Wins!")
elif Player1=="scissors" and Player2 =="rock":
    print("Player2 Wins!")
elif Player1=="scissors" and Player2 =="Paper":
    print("Player1 Wins!")
elif Player1 == Player2:
    print("Its a tie!") 
else:
    print("something went wrong") 