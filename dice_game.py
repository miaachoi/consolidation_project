import random # Importing random module for generating random dice rolls 
import pandas as pd # Importing pandas for data tracking 
import numpy as np # Importing numpy for calculations 
import time # Importing time module for timing each player's turn 
import seaborn as sns # Importing seaborn for data visualization 
import matplotlib.pyplot as plt # Importing matplotlib for plotting graphs 

players = {} # Dictionary to store player names and scores
score_data = [] # List to track scores each round, which will be used later for analysis 

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

def plot_scores(players): 
    """Plots the current scores of all game players."""
    sns.barplot(x=list(players.keys()), y=list(players.values()), hue=list(players.keys()), palette="viridis", legend=False)
    plt.title("Player Scores")
    plt.xlabel("Players")
    plt.ylabel("Scores")
    plt.show()

# Initialize game variables 
num_players = int(input("Enter the number of players: ")) # Get number of players
target_score = int(input("Enter the target score to win: ")) # Get target score to win 

# Add players to the game 
for i in range(1, num_players + 1):
    name = input(f"Enter Player {i}'s name: ") # Get each player's name 
    players[name] = 0 # Initialize each player's score to 0 

game_winner = None # Variable to track who the winner is 
round_num = 1 # Start the round counter

# Main game loop 
while not game_winner: 
    """
    Main game loop where players take turns rolling dice and gaining points until one reaches the target score.
    """
    print(f"\nRound {round_num}") # Displays the current round number

    for player in players: 
        print(f"\n{player}'s turn!") # Says whose turn it is 
        turn_start = time.process_time() # Start the timer for player's turn

        dice = roll_dice() # Roll three dice at the start of the turn 
        fixed = set() # Set to store "fixed" dice (cannot be rerolled)

        # Check for dice that are fixed (appear two or more times)
        for die in set(dice):
            if dice.count(die) >= 2:
                fixed.add(die) 

        while True: 
            print(f"Rolled dice: {dice}") # Show the dice rolled in this turn
            print(f"Fixed dice: {list(fixed)}") # Show the fixed dice that won't be rerolled

            # Check if all dice are the same (player "tupled out") and end the turn with 0 points
            if len(set(dice)) == 1: 
                print(f"{player} 'tupled out'! Turn ends with 0 points.")
                break # End the player's turn if all dice are the same 

            # Identify unfixed dice (the dice not in the fixed set) 
            unfixed_dice = [die for die in dice if die not in fixed]
            
            # Check if the player has no unfixed dice left to reroll 
            if not unfixed_dice: # No unfixed dice left to reroll # No unfixed dice left to reroll 
                print(f"{player} decides to stop. Total points: {sum(dice)}")
                players[player] += sum(dice) # Add score to player's total 
                break 

            # Ask the player if they want to reroll the unfixed dice or stop
            reroll = input(f"Do you want to reroll unfixed dice ({unfixed_dice})? (y/n): ").lower() 
            
            if reroll == 'y': # Player decides to reroll 
                new_roll = roll_dice(len(unfixed_dice))  # Roll only the unfixed dice 
                dice = list(fixed) + new_roll # Combine fixed dice with new rolls
                print(f"New roll: {new_roll}") # Display result of the new roll 
                
                # Update fixed dice if any appear twice in the new roll 
                for die in set(dice):
                    if dice.count(die) >=2 and die not in fixed: # If any die appears twice now, it is considered fixed
                        fixed.add(die)

            else: # Player decides to stop rolling and keep the points
                print(f"{player} decides to stop. Total points: {sum(dice)}") # Player stops and adds up their score 
                players[player] += sum(dice) # Add points to player's total score
                break # End the player's turn 

        turn_end = time.process_time() # Stop timing player's turn 
        print(f"{player}'s turn took {turn_end - turn_start:.2f} seconds.")

        # Tracking score data in a simple list, will be used for analysis later
        score_data.append({"Player": player, "Round": round_num, "Score": sum(dice)})

        # Check if the player has reached or exceeded the target score
        if players[player] >= target_score: 
            game_winner = player # Say who the winner is 
            break 

    # Display the scores after each round 
    print("Displaying scores...")
    print("Please close the plot window to continue the game.") # Notify the user"
    plot_scores(players)

    # Calculate average score using NumPy
    average_score = np.mean([p["Score"] for p in score_data])
    print(f"Average score after round {round_num}: {average_score:.2f}")

    # Add a delay before starting the next round 
    time.sleep(2)

    round_num += 1 # Increment the round counter 

# Declare the winner 
print(f"\nCongratulations, {game_winner}! You won with {players[game_winner]} points!")

score_df = pd.DataFrame(score_data)
"""
Converts 'score_data' list, which contains dictionaries of player scores, into pandas DataFrame.
This format allows for a more flexible handling of the data for analysis and export. 
"""
score_df.to_csv("tuple_scores.csv", index=False) # Exports score data to CSV file, without including the index
print("Game scores saved to 'tuple_scores.csv'.")