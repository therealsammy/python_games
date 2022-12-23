import random


def get_choices():
    players_choice = input("Enter a choice -> rock, paper, scissors: ")

    options = ["rock", "paper", "scissors"]

    computers_choice = random.choice(options)

    choices = {
        "player": players_choice,
        "computer": computers_choice
    }

    return choices


def check_win(player, computer):
    player = player.lower()

    players_choice = ["rock", "paper", "scissors"]

    if player not in players_choice:
        return ("Must be rock, paper or scissors")

    print(f"You chose {player}, computer chose {computer}")

    if player == computer:
        return "It's a tie!"
    elif player == "rock":
        if computer == "scissors":
            return "Rock smashes scissors! You win!"
        else:
            return "Paper covers rock! You lose!"
    elif player == "scissors":
        if computer == "paper":
            return "Scissors cuts paper! You win!"
        else:
            return "Rock smashes scissors! You lose!"
    elif player == "paper":
        if computer == "rock":
            return "Paper covers rock! You win!"
        else:
            return "Scissors cuts paper! You lose!"


choices = get_choices()

result = check_win(choices["player"], choices["computer"])

print(result)
