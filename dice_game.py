import random
import sys

def play_turn():
    """
    Stimulates a player's turn in the dice game.
    Rolls three dice, checks for any duples, and allows the player to reroll unmatched dice for a better score. 
    Returns the total score for the turn.

    """
    dice_amount = 3
    your_roll = random.choices([1, 2, 3, 4, 5, 6], k=dice_amount)
    print(f"Your roll: {your_roll}")

    # Check if all three dice are the same (tuple out) 
    if your_roll[0] == your_roll[1] and your_roll[1] == your_roll[2]:
        print("You tupled out! Your turn ends with 0 points.")
        return 0 # No re-rolling, return score of 0 for this turn 
    
    # Initialize fixed dice list
    fixed_dice = []

    # Check if two dice are the same, then fix them
    if your_roll[0] == your_roll[1]:
        fixed_dice = [your_roll[0], your_roll[1]]
        fixed_dice.append(random.choice([1, 2, 3, 4, 5, 6]))
    elif your_roll[1] == your_roll[2]:
        fixed_dice = [your_roll[1], your_roll[2]]
        fixed_dice.insert(0, random.choice([1, 2, 3, 4, 5, 6]))
    elif your_roll[0] == your_roll[2]:
        fixed_dice = [your_roll[0], your_roll[2]]
        fixed_dice.insert(1, random.choice([1, 2, 3, 4, 5, 6])) 
    else:
        print("No matching dice, no reroll. Final score for this turn.")
        return sum(your_roll) 
    
    reroll = input("Do you want to reroll the remaining die(s)? (y/n): ").strip().lower() 
    while reroll not in ['y', 'n']:
        print("Invalid input. Please enter 'y' or 'n':")
        reroll = input().strip().lower()

    if reroll == 'y' and len(fixed_dice) < 3: 
        remaining_dice = 3 - len(fixed_dice)
        for _ in range(remaining_dice): 
            fixed_dice.append(random.choice([1, 2, 3, 4, 5, 6]))
        print(f"New roll: {fixed_dice}")
    elif reroll == 'n':
        print(f"Final score for this turn: {sum(fixed_dice)}")

    return sum(fixed_dice)

def play_game(target_score=100):
    """
    Plays the dice game, where a player takes turns rolling dice. The game ends when the player's score reaches the target score.
    """
    total_score = 0 

    while total_score < target_score: 
        print("\nNew turn!")
        try:
            score = play_turn() 
            total_score += score
            print(f"Total score: {total_score}")
        except Exception as e: 
            print(f"An unexpected error occurred during the turn: {e}")
            break
        if total_score >= target_score:
            print("Congratulations, you won!")
            break 
target_score = 100 

if len(sys.argv) > 1:
    try:
        target_score = int(sys.argv[1])
        print(f"Custom target score set to: {target_score}")
    except ValueError:
        print("Invalid target score provided. Using default of 100.")
play_game(target_score)