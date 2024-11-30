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

winner = None 

while not winner: 
    for player in players: 
        print(f"\n{player}'s turn!")
        dice = roll_dice()
        fixed = set() 

        for die in set(dice):
            if dice.count(die) >= 2:
                fixed.add(die) 

        while True: 
            print(f"Rolled dice: {dice}")
            print(f"Fixed dice: {list(fixed)}")

            if len(set(dice)) == 1: 
                print(f"{player} 'tupled out'! Turn ends with 0 points.")
                break
            # Identify unfixed dice 
            unfixed_dice = [die for die in dice if die not in fixed]
            if not unfixed_dice: # No unfixed dice left to reroll
                print(f"{player} decides to stop. Total points: {sum(dice)}")
                players[player] += sum(dice) # Add score 
                break 

            reroll = input(f"Do you want to reroll unfixed dice ({unfixed_dice})? (y/n): ").lower() 
            
            if reroll == 'y': # Player wants to reroll
                # Roll only the unfixed dice 
                new_roll = roll_dice(len(unfixed_dice))
                # Combine the fixed dice and new roll 
                dice = list(fixed) + new_roll
                print(f"New roll: {new_roll}")
        
                for die in set(dice):
                    if dice.count(die) >=2 and die not in fixed: 
                        fixed.add(die)
            else: 
                print(f"{player} decides to stop. Total points: {sum(dice)}")
                players[player] += sum(dice) 
                break 
    
        if players[player] >= target_score: 
            winner = player
            break 
    display_scores(players)
print(f"\nCongratulations, {winner}! You won with {players[winner]} points!")

