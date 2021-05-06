# Farkle Simulator
    created by Samuel Luke
    
This is a command-line program that simulates a single player game of Farkle, the popular dice rolling card game. It can be played normally or be used to simulate any number of games using a certain strategy. 

This was built as a way to find the ideal strategy to win faster than your opponents. Statistics from the simulation are available in the accompanied files "keepAll.txt", "keepHighest.txt", and "farkle stats.xlsx"

## Rules
The goal is to score 10000 points over a course of turns. Each player rolls 6 dice and can then decide to keep or reroll as many as they desire, as long as each roll adds some amount to their score. They are allowed to continue rolling as many times as they want, until they choose to pass and keep their score, or roll a hand with no scoring dice, in which case their turn is over and they add no points to their total score. If all 6 dice are scoring, then the player is allowed to roll all 6 again. 

## Scoring
    1 	            100 points
    5 	            50 points
    Three 1s 	    300 points
    Three 2s 	    200 points
    Three 3s 	    300 points
    Three 4s 	    400 points
    Three 5s 	    500 points
    Three 6s 	    600 points
    3 Pairs 	    1500 points
    1-6 Straight  	1500 points
    Full House      1500 points
    2 Triplets      2500 points
    4 of a kind     1000 points
    5 of a kind     2000 points
    6 of a kind     3000 points


## Usage
python farkle.py [strategy {user(default), keepHighest, keepAll}] [target {targetScore(default), targetDice}] [number of iterations] [hideStats]


## Simulation
This program can simulate any number of games where the program decides when to roll or keep the dice based on a number of strategies discussed below. The program will average the results and display statistics of what rolls were generated and what the average number of turns it took to reach 10000 points. 

    user (default): The user interacts with the console by answering prompts to play their own game of farkle

    keepHighest: This option will discard all but the highest scoring dice. For example, if a hand with 3 of a kind and 1 five is rolled, the simulation will keep the 3 of a kind but reroll the five and other dice. 

    keepAll: This option will keep all dice that add to the total score of the hand. For example, if a hand with 3 of a kind and 1 five is rolled, the simulation will keep those four dice and only reroll the non-scoring dice.

The program also has options to specify a "target", which when reached will tell the program to stop rolling and save the current score. The program steps through a number of these targets to pinpoint the ideal stopping point based on the lowest number of average turns to win the game.

    targetScore (default): this option will simulate games and stop rolling once a certain score is met. For example, if the target score is 500, the program will continue to roll until the turn score is greater than or equal to 500, at which point it will stop. It will step through games with a target score of 0-1000 in increments of 50.

    targetDice: this option will simulate games and stop rolling once it is below a certain number of dice available to roll. For example, if the target dice is 2, the program will continue to roll until it has 2 or fewer dice that did not contribute to the score. It will step through games with a target score of 1-6. 

The number of iterations allows the user to specify how many games should be ran and averaged. The higher the number, the more accurate the results as variation is limited, but a longer runtime will be required. 

hideSats doesn't print the stats to allow for more compact viewing. Off by default