import random

def play_turn():
    dice_amount = 3
    your_roll = random.choices([1, 2, 3, 4, 5, 6], k=dice_amount)
    print(f"Initial roll: {your_roll}")

    # Check if all three dice are the same (tuple out) 
    if your_roll[0] == your_roll[1] and your_roll[1] == your_roll[2]:
        print("You tupled out! Your turn ends with 0 points.")
        return 0
    
    # Initialize fixed dice list
    fixed_dice = []

    # Check if two dice are the same, then fix them
    if your_roll[0] == your_roll[1]:
        fixed_dice = [your_roll[0], your_roll[1]]
        third_die = random.choice([1, 2, 3, 4, 5, 6])
        fixed_dice.append(third_die)
    elif your_roll[1] == your_roll[2]:
        fixed_dice = [your_roll[1], your_roll[2]]
        third_die = random.choice([1, 2, 3, 4, 5, 6])
        fixed_dice.insert(0, third_die) 
    elif your_roll[0] == your_roll[2]:
        fixed_dice = [your_roll[0], your_roll[2]]
        third_die = random.choice([1, 2, 3, 4, 5, 6])
        fixed_dice.insert(1, third_die)
    else:
        print("No matching dice, all dice are rerolled.")
        fixed_dice = your_roll

    print(f"Fixed dice: {fixed_dice}")
    return sum(fixed_dice)
 
def play_game():
    total_score = 0 

    while total_score < 100:
        print("\nNew turn!")
        score = play_turn()
        total_score += score 
        print(f"Total score: {total_score}")
        
        if total_score >= 100:
            print("Congratulations, you won!")
            break 
        
play_game()