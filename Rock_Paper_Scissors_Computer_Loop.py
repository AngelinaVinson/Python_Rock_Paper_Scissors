# Import Needed Packages
import random
player_wins = 0
computer_wins = 0

while player_wins < 5 and computer_wins < 5:
	
	print("Rock, Paper, Scissors")


	# Play Selects/Inputs Move
	player = input("Player, make your move: ").lower()
	
	# Computer Selects Move (Randomly)
	rand_num = random.randint(0,2)
	if rand_num == 0:
		computer = "rock"
	elif rand_num == 1:
		computer = "scissors"
	else:
		computer = "paper"
	print("computer plays ".format(computer))
	


	if player == computer:
		print("draw")
	elif player == "rock":
		if computer == "paper":
			print("Computer wins")
			computer_wins += 1
		elif computer == "scissors":
			print("Player wins")
			player_wins += 1
		print("Player Score: {} \n Computer Score: {} ".format(player_wins, computer_wins))
	elif player == "paper":
		if computer == "rock":
			print("Player  wins")			
			player_wins += 1
		elif computer == "scissors":
			print("Computer wins")
			computer_wins += 1
		print("Player Score: {} \n Computer Score: {} ".format(player_wins, computer_wins))
	elif player == "scissors":
		if computer == "rock":
			print("Computer wins")
			computer_wins += 1
		elif computer == "paper":
			print("Player Wins")
			player_wins += 1
		print("Player Score: {} \n Computer Score: {} ".format(player_wins, computer_wins))
	else:
		print("something went wrong")
		
if player_wins > computer_wins:
	print("YAY, You won!")
elif player_wins == computer_wins:
	print("Draw")
else:
	("No, Computer Won")
	

