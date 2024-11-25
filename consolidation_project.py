import random

def play_turn(): 
    dice_amount = 3
    your_roll = random.choices([1, 2, 3, 4, 5, 6], k=dice_amount)
    print(f"Initial roll: {your_roll}")

    prev_duple = [None, None, None]

    if len(your_roll) < 3:
           your_roll[0] = prev_duple[0]
           prev_duple[1] = prev_duple[2] = prev_duple[0]
    
    elif len(your_roll) == 3 and your_roll[0] == your_roll[1]: 
         print("The first two dice are the same!")
         prev_duple[0], prev_duple[1], prev_duple[2] = your_roll[0], your_roll[1], your_roll[2]
    else: 
        prev_duple[0], prev_duple[1], prev_duple[2] = your_roll[0], your_roll[1], your_roll[2]

    print(f"Updated roll after checking duplicates: {your_roll}")
    print(f"Previous duplicates: {prev_duple}")

    return your_roll 

def play_game():
    total_score = 0 
    while total_score < 100: 
        print("\nNew turn!")
        score = play_turn()
        total_score += sum(score)
        print(f"Total score: {total_score}")

        if total_score >=100: 
            print("Congratulations, you won!")
            break 
play_game()
