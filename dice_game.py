import random 

def play_turn():
    dice_amount = 3
    your_roll = random.choices([1, 2, 3, 4, 5, 6], k=dice_amount)
    print(f"Initial roll: {your_roll}")

if (your_roll[0] == your_roll[1]) and (your_roll[1] == your_roll[2]):
    print("You tupled out! Your turn ends with 0 points.")

    if fixed_dice = [your_roll[0], your_roll[1]]
    elif your_roll[1] == your_roll[2]:
        fixed_dice = [your_roll[0], your_roll[2]]
    return fixed_dice

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