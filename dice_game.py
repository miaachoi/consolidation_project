import random # Importing random module for generating random dice rolls 

# Display the game rules 
print("Welcome to the 'Tuple Out' Dice Game!")
print("Rules: Get the highest score without 'tupling out'.")

def roll_dice(dice_amount=3):
    """Rolls a specified number of dice and returns the results as a list."""
    return[random.randint(1, 6) for _ in range(dice_amount)]

def display_scores(players):
    """Displays the current scores of all players."""
    print("\nCurrent Scores:")
    for player, score in players.items():
        print(f"{player}: {score} points")

# Initialize game variables 
players = {}
num_players = int(input("Enter the number of players: "))
target_score = int(input("Enter the target score to win: "))

# Add players to the game 
for i in range(1, num_players + 1):
    name = input(f"Enter Player {i}'s name: ")
    players[name] = 0