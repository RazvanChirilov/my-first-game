from random import randint
print("rock")
print("paper")
print("scissors")

player = input("Player make your move: ").lower()
random_num = randint(0, 2)
if random_num == 0:
    computer = "rock"
elif random_num == 1:
    computer = "paper"
else:
    computer = "scissors"

print(f"Computer plays {computer} ")

# de aici ar trebui sa imi apara rezultatul jocului

if player == computer:
    print("Sorry it`s draw")
elif player == "rock":
    if computer == "scissors":
        print("You win")
    else:
        print("Computer wins!")
elif player == "paper":
    if computer == "rock":
        print("You win")
    else:
        print("Computer wins")
elif player == "scissors":
    if computer == "rock":
        print("Computer wins")
    else:
        print("You win")
else:
    print("Please enter a valid move")

