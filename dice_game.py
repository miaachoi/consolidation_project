import random # Importing random module for generating random dice rolls 
import sys # Importing sys to allow command-line arguments for custom target score 

def play_turn():
    """
    Stimulates a player's turn in the dice game.
    Rolls three dice, checks for any duples, and allows the player to reroll unmatched dice for a better score. 
    Returns the total score for the turn.

    """
    dice_amount = 3 # Number of dice rolled per turn 
    your_roll = random.choices([1, 2, 3, 4, 5, 6], k=dice_amount) # Roll three dice 
    print(f"Your roll: {your_roll}") # Display initial dice roll 

    # Check if all three dice are the same (tuple out) 
    if your_roll[0] == your_roll[1] and your_roll[1] == your_roll[2]:
        print("You tupled out! Your turn ends with 0 points.")
        return 0 # No re-rolling, return score of 0 for this turn 
    
    # Initialize fixed dice list to keep track of dice that won't be rerolled 
    fixed_dice = []

    # Check if two dice are the same, then keep them fixed
    if your_roll[0] == your_roll[1]:
        fixed_dice = [your_roll[0], your_roll[1]] # Store matching dice 
        fixed_dice.append(random.choice([1, 2, 3, 4, 5, 6])) # Reroll the third dice 
    elif your_roll[1] == your_roll[2]:
        fixed_dice = [your_roll[1], your_roll[2]] # Store matching dice 
        fixed_dice.insert(0, random.choice([1, 2, 3, 4, 5, 6])) # Reroll the first die 
    elif your_roll[0] == your_roll[2]:
        fixed_dice = [your_roll[0], your_roll[2]] # Store matching dice 
        fixed_dice.insert(1, random.choice([1, 2, 3, 4, 5, 6])) # Reroll the second die 
    else:
        print("No matching dice, no reroll. Final score for this turn.")
        return sum(your_roll) # No reroll if no matching dice, return the sum of the initial roll 
    # Ask the player if they want to reroll the remaining die(s)
    reroll = input("Do you want to reroll the remaining die(s)? (y/n): ").strip().lower() 
    while reroll not in ['y', 'n']: # Ensure input is valid 
        print("Invalid input. Please enter 'y' or 'n':")
        reroll = input().strip().lower()
    # If player chooses to reroll, reroll the remaining dice 
    if reroll == 'y' and len(fixed_dice) < 3: 
        remaining_dice = 3 - len(fixed_dice) # Calculate how many dice need to be rerolled
        for _ in range(remaining_dice): # Reroll remaining dice
            fixed_dice.append(random.choice([1, 2, 3, 4, 5, 6]))
        print(f"New roll: {fixed_dice}") # Display new dice roll 
    elif reroll == 'n':
        print(f"Final score for this turn: {sum(fixed_dice)}") # If no reroll, show the final score for the turn 

    return sum(fixed_dice) # Return the total score for the turn 

def play_game(target_score=100):
    """
    Plays the dice game, where a player takes turns rolling dice. The game ends when the player's score reaches the target score.
    """
    total_score = 0 # Initialize the total score 

    while total_score < target_score: # Keep playing until the total score reaches the target
        print("\nNew turn!") # Indicate the start of a new turn 
        try:
            score = play_turn() # Play a turn and get the score 
            total_score += score # Add the score to the total 
            print(f"Total score: {total_score}") # Display updated total score 
        except Exception as e: # Handle any errors that may occur during the turn 
            print(f"An unexpected error occurred during the turn: {e}")
            break
        if total_score >= target_score:
            print("Congratulations, you won!")
            break 
# Set default target score to 100
target_score = 100 

# Check if a custom target score is provided via command-line arguments 
if len(sys.argv) > 1:
    try:
        target_score = int(sys.argv[1]) # Set custom target score 
        print(f"Custom target score set to: {target_score}")
    except ValueError:
        print("Invalid target score provided. Using default of 100.")
play_game(target_score) # Start game with the target score 