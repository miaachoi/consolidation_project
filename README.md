The "Tuple Out Dice Game" is a competitive dice game where players aim to reach a target score without 'tupling out' (rolling all dice to the same value). Players take turns rolling three dice. If two dice match, they are considered "fixed," and only the remaining dice can be rerolled. Rolling all three dice to the same value ("tupled out") ends the turn with zero points. After each roll, players can decide to reroll unfixed dice or stop and add their current total to their score. The game checks after each turn if a player's score has reached or exceeded the target, declaring them the winner. At the end of the game, the results are exported to a CSV file. 

Key Features: 
- The game tracks how long each player's turn lasts using time.process_time(). 
- A 2-second delay between rounds provides pacing.
- After every round, a bar chart is generated to visualize the players' scores using Seaborn.
- NumPy calculates the average scores after each round, showing insight into player performance.
- Player scores are tracked using Pandas, and at the end of the game, all score data is exported to a CSV file for further analysis or record-keeping. 

Example Game Play:
1. Enter the number of players: 2
2. Enter the target score to win: 50
3. Player 1 rolls: [1, 2, 2]. Fixed dice: [2].
4. Player 1 decides to reroll. New roll: [2, 4].
5. Player 1's turn ends. They then add the total points from their roll to their score.
6. After every round, the scores are updated and displayed in a bar chart. 
