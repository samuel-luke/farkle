import random
import time
import os
import sys


class Farkle:
    def __init__(self, strategy="user", targetScore = 10000, targetDice = -1):
        self.strategy = strategy
        self.targetScore = targetScore
        self.targetDice = targetDice
        self.score = 0
        self.rule = "nothing"
        self.hand = []
        self.counts = []
        self.scoringDice = 0
        self.turnScore = 0
        self.dice = 6
        self.stats = {
            "Turns": 0,
            "Total Score": 0,
            "nothing": 0,
            "ones & fives": 0,
            "3 Ones": 0,
            "3 Twos": 0,
            "3 Threes": 0,
            "3 Fours": 0,
            "3 Fives": 0,
            "3 Sixes": 0,
            "4 of a kind": 0,
            "5 of a kind": 0,
            "6 of a kind": 0,
            "Straight": 0,
            "3 Pairs": 0,
            "2 Triplets": 0,
            "Full House": 0,
        }
        
        
    def title(self):
        os.system('cls')
        print("Total score:", self.stats["Total Score"])
        print("Turn:", self.stats["Turns"])
        print("Turn score:", self.turnScore)
        print(
            """
                                     ______         _    _                ____
                                    |  ____|       | |  | |              /\\' .\    _____
                                    | |__ __ _ _ __| | _| | ___         /: \___\  / .  /\\
                                    |  __/ _` | '__| |/ / |/ _ \        \\' / . / /____/..\\
                                    | | | (_| | |  |   <| |  __/         \/___/  \\'  '\\  /
                                    |_|  \__,_|_|  |_|\_\_|\___|                  \\'__'\\/
            """
        )


    def roll(self):
        if self.strategy == "user":
            input("Press enter to roll")
            
        self.hand = []
        for i in range(0, self.dice):
            self.hand.append(random.randint(1, 6))
        
        if self.strategy == "user":
            print()
            self.title()

        self.hand.sort()
        if self.strategy == "user":
            print("You rolled:", self.hand)

        self.counts = []
        for i in range(0, len(self.hand)):
            self.counts.append(self.hand.count(i+1))

        self.counts.sort()


    def scoring(self):
        self.score = 0
        self.rule = "nothing"
        self.scoringDice = 0

        if len(self.hand) >= 3:
            # 3 Ones
            if self.hand.count(1) == 3:
                self.rule = "3 Ones"
                self.score = 0

            # 3 Twos
            if self.hand.count(2) == 3:
                self.rule = "3 Twos"
                self.score = 200
                self.scoringDice += 3

            # 3 Threes
            if self.hand.count(3) == 3:
                self.rule = "3 Threes"
                self.score = 300
                self.scoringDice += 3

            # 3 Four
            if self.hand.count(4) == 3:
                self.rule = "3 Fours"
                self.score = 400
                self.scoringDice += 3

            # 3 Fives
            if self.hand.count(5) == 3:
                self.rule = "3 Fives"
                self.score = 350

            # 3 Sixes
            if self.hand.count(6) == 3:
                self.rule = "3 Sixes"
                self.score = 600
                self.scoringDice += 3

            # 4 of a kind
            if self.counts[-1] == 4:
                self.rule = "4 of a kind"
                self.score = 1000
                self.scoringDice += 4
                if self.hand.count(1) == 4:
                    self.score -= 400
                    self.scoringDice -= 4
                if self.hand.count(5) == 4:
                    self.score -= 200
                    self.scoringDice -= 4

            # Straight
            if len(self.hand) == 6:
                ordered = 0
                for i in range(0, 6):
                    if self.hand[i] == i+1:
                        ordered += 1
                if ordered == 6:
                    self.rule = "Straight"
                    self.score = 1350 # 1500 - 100 - 50 for 1 and 5, which are already counted
                    self.scoringDice = 4 # 6 - 2 for 1 and 5, which are already counted

            # 3 Pairs
            if self.counts[-3] == 2 and self.counts[-2] == 2 and self.counts[-1] == 2:
                self.rule = "3 Pairs"
                self.score = 1500
                self.scoringDice = 6
                if self.hand.count(1) == 2:
                    self.score -= 200
                    self.scoringDice -= 2
                if self.hand.count(5) == 2:
                    self.score -= 100
                    self.scoringDice -= 2
                    
            # Full House
            if self.counts[-1] == 4 and self.counts[-2] == 2:
                self.rule = "Full House"
                self.score = 1500
                self.scoringDice = 6
                if self.hand.count(1) == 2:
                    self.score -= 200
                    self.scoringDice -= 2
                if self.hand.count(5) == 2:
                    self.score -= 100
                    self.scoringDice -= 2
                if self.hand.count(1) == 4:
                    self.score -= 400
                    self.scoringDice -= 4
                if self.hand.count(5) == 4:
                    self.score -= 200
                    self.scoringDice -= 4

            # 5 of a kind
            if self.counts[-1] == 5:
                self.rule = "5 of a kind"
                self.score = 2000
                self.scoringDice = 5
                if self.hand.count(1) == 5:
                    self.score -= 500
                    self.scoringDice -= 5
                if self.hand.count(5) == 5:
                    self.score -= 250
                    self.scoringDice -= 5

            # 2 Triplets
            if self.counts[-1] == 3 and self.counts[-2] == 3:
                self.rule = "2 Triplets"
                self.score = 2500
                self.scoringDice = 6
                if self.hand.count(1) == 3:
                    self.score -= 300
                    self.scoringDice -= 2
                if self.hand.count(5) == 3:
                    self.score -= 150
                    self.scoringDice -= 2

            # 6 of a kind
            if self.counts[-1] == 6:
                self.rule = "6 of a kind"
                self.score = 3000
                self.scoringDice = 6
                if self.hand.count(1) == 6:
                    self.score -= 600
                    self.scoringDice -= 6
                if self.hand.count(5) == 6:
                    self.score -= 300
                    self.scoringDice -= 6

        for i in range(0, len(self.hand)):
            if self.hand[i] == 5:
                if self.rule == "nothing":
                    self.rule = "ones & fives"
                self.scoringDice += 1
                self.score += 50

            if self.hand[i] == 1:
                if self.rule == "nothing":
                    self.rule = "ones & fives"
                self.scoringDice += 1
                self.score += 100


    def turn(self):
        self.stats["Turns"] += 1
        self.dice = 6
        while(1):
            self.roll()
            self.scoring()
            if self.strategy == "user":
                print("This hand contains " + self.rule + "! Worth", self.score, "points\n")
            
            if self.score == 0:
                if self.strategy == "user":
                    print("Sorry! Your turn is over")
                
                self.turnScore = 0
                break

            self.turnScore += self.score                
            self.dice = 0
                
            user_input = "r"
            if self.strategy == "user":
                if self.scoringDice >= len(self.hand):
                    print("All your dice are scoring! You can roll all six again!")
                user_input = input("Type [r] to roll again OR [s] to stop and secure your points:")
            else:
                if self.dice == 6:
                    user_input = "r"
                if self.dice <= self.targetDice:
                    user_input = "s"
                if self.turnScore >= self.targetScore:
                    user_input = "s"
                
            if user_input == "s":
                break
            else:
                if self.scoringDice >= len(self.hand):
                    self.dice = 6
                    continue
                
                if self.strategy == "user":
                    print("Which die do you want to reroll? \nEnter one per line. Press enter to reroll all remaining non-scoring die. You must keep at least one scoring die")
                while(len(self.hand) > 1):
                    user_input = ""
                    if self.strategy == "user":
                        user_input = input(":")
                    elif self.strategy == "keepHighest":
                        while(1):
                            self.scoring()
                            current_score = self.score
                            lowestScoring = None
                            lowestScore = 0
                            toRemove = []
                            for d in self.hand:
                                self.hand.remove(d)
                                self.scoring()
                                self.hand.append(d)
                                self.hand.sort()
                                if self.score == current_score:
                                    toRemove.append(d)
                                elif self.score < current_score and current_score-self.score > lowestScore:
                                    lowestScore = current_score-self.score
                                    lowestScoring = d
                            # print("Hand:", self.hand, "Lowest scoring dice:", lowestScoring, "worth", lowestScore, "points")
                            self.scoring()
                            current_score = self.score     
                            self.hand.remove(lowestScoring)
                            self.scoring()
                            if self.score == 0: # Prevents removing the last scoring dice
                                self.hand.append(lowestScoring)
                                self.hand.sort()
                                self.scoring()
                                break
                            else:
                                for d in toRemove:
                                    self.hand.remove(d)
                                self.scoring()
                                self.dice += len(toRemove)
                        break
                        
                    if user_input == "": # Remove everything that is not scoring
                        self.scoring()
                        current_score = self.score
                        toRemove = []
                        for d in self.hand:
                            self.hand.remove(d)
                            self.scoring()
                            self.hand.append(d)
                            self.hand.sort()
                            if self.score == current_score:
                                toRemove.append(d)
                        for d in toRemove:
                            self.hand.remove(d)
                        self.scoring()
                        self.dice += len(toRemove)
                        break
                    else: # Remove a specific die
                        val = 0
                        try:
                            val = int(user_input)
                        except ValueError:
                            print("Please enter a number from 1-6")
                            continue
                        if val in self.hand:
                            self.hand.remove(val)
                            self.scoring()
                            if self.score != 0:
                                self.dice += 1
                            else:
                                self.hand.append(val)
                                self.hand.sort()
                                print("You can't remove this die! Otherwise your score for this round would be zero. Try again")
                        else:
                            print("Please choose a number from a dice in your hand")
                
        self.stats["Total Score"] += self.turnScore
        if self.strategy == "user":
            print("You scored", self.turnScore, "points this turn!")
        self.turnScore = 0
            
        self.stats[self.rule] += 1
                
        
    def play(self):
        while(1):
            self.turn()
            
            if self.stats["Total Score"] >= 10000:
                if self.strategy == "user":
                    print("\n--- You won!!! ---\n")
                    for rule in self.stats:
                        print(rule, "  \t\t", self.stats[rule], "    \t\t", str(round(self.stats[rule]/self.stats["Turns"], 5)) + "%")
                    input("Press enter to exit")
                return self.stats
        

def main():
    iterations = 1000
    strategy = "user"
    goal = "Target Score"
    target = 1050
    step = 50
    hideStats = False
    
    if "-h" in sys.argv:
        print("Usage: python farkle.py [strategy {user(default), keepHighest, keepAll}] [target {targetScore(default), targetDice}] [number of iterations] [hideStats(default off)]")
        print("See the README.md file for more instructions")
        return
        
    if len(sys.argv) >= 2:
        if sys.argv[1] == "user" or sys.argv[1] == "keepHighest" or sys.argv[1] == "keepAll":
            strategy = sys.argv[1]
        else:
            print("Unknown argument: ", sys.argv[1])
            return
        
    if len(sys.argv) >= 3:
        if sys.argv[2] == "targetScore":
            goal = "Target Score"
            target = 1050
            step = 50
        elif sys.argv[2] == "targetDice":
            goal = "Target Dice"
            target = 6
            step = 1
        else:
            print("Unknown argument:", sys.argv[2])
            return
        
    if len(sys.argv) >= 4:
        try:
            iterations = int(sys.argv[3])
        except ValueError:
            print("Please enter an integer for the number of iterations", sys.argv[3])
            return
            
    if len(sys.argv) == 5:
        if sys.argv[4] == "hideStats":
            hideStats = True
        else:
            print("Unknown argument:", sys.argv[4])
            return
            
        
    if strategy != "user":
        print("\t ----- Beginning Simulation ----- ")
        for i in range (0, target, step):
            total_stats = {
                "Games": 0,
                "Turns": 0,
                "nothing": 0,
                "ones & fives": 0,
                "3 Ones": 0,
                "3 Twos": 0,
                "3 Threes": 0,
                "3 Fours": 0,
                "3 Fives": 0,
                "3 Sixes": 0,
                "4 of a kind": 0,
                "5 of a kind": 0,
                "6 of a kind": 0,
                "Straight": 0,
                "3 Pairs": 0,
                "2 Triplets": 0,
                "Full House": 0,
            }
        
            if goal == "Target Dice":
                print("\n---", goal, ":", i+1, " --- ")
            else: 
                print("\n---", goal, ":", i, " --- ")
            for j in range(iterations):
                f = None
                if goal == "Target Dice":
                    f = Farkle(strategy=strategy, targetDice=i+1)
                else:
                    f = Farkle(strategy=strategy, targetScore=i)
                stats = f.play()
                for rule in stats:
                    if rule == "Total Score":
                        continue
                    total_stats[rule] += stats[rule]
                total_stats["Games"] += 1
            
            if not hideStats:
                for rule in total_stats:
                    if rule == "Games" or rule == "Turns":
                        print(rule, "  \t\t", total_stats[rule])
                        continue
                    print(rule, "  \t\t", total_stats[rule], "     \t\t", str(round(total_stats[rule]/total_stats["Turns"]*100, 2)) + "%")
            print("Average Turns:", total_stats["Turns"]/total_stats["Games"])
    else:
        f = Farkle()
        f.play()


if __name__ == "__main__":
    main()
