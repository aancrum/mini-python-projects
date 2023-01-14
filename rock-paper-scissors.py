from random import randint

# List of winning patterns
# Scissors cuts Paper, Paper covers Rock, Rock crushes Scissors

win = [("scissors", "paper"), ("paper", "rock"), ("rock", "scissors")]

# INSTRUCTIONS
print("There are 3 rounds."
      "You are playing against the computer."
      "You will win if you have a higher point."
      "Enter scissors, paper, or rock."
      "Good Luck, may the best player win. :)")

choices = ["scissors", "paper", "rock"]
# assign the computer play, 0-2 represents the position of the pick
computer = choices[randint(0, 2)]
# set variable to count number of rounds
count = 0
# set variable to count player's points
plPoints = 0
# set variable to count computers' points
comPoints = 0
# set the number of rounds
while count != 3:
    # set player input
    player = input("Rock, Paper, Scissors? ")
    if player == computer:
        print("Tie!")
    elif player == "Rock":
        if computer == "Paper":
            print("You lose!", computer, "covers", player)
            comPoints += 1
        else:
            print("You win!", player, "smashes", computer)
            plPoints += 1
    elif player == "Paper":
        if computer == "Scissors":
            print("You lose!", computer, "cut", player)
            comPoints += 1
        else:
            print("You win!", player, "covers", computer)
            plPoints += 1
    elif player == "Scissors":
        if computer == "Rock":
            print("You lose...", computer, "smashes", player)
            comPoints += 1
        else:
            print("You win!", player, "cut", computer)
            plPoints += 1
    else:
        print("That's not a valid play. Check your spelling!")
    if plPoints >= comPoints:
        print("Congratulations, you are the champion!")
    else:
        print("Sorry you have lost, try again.")
    count += 1
    player = False
    computer = choices[randint(0, 2)]
