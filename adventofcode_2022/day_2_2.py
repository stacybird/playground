# Advent of code 2.2
# Happy Advent!
#                "The first column is what your opponent is going to play: A for Rock, B for Paper, and C for Scissors."
# The score for a single round is the score for the shape you selected (1 for Rock, 2 for Paper, and 3 for Scissors)
# plus the score for the outcome of the round (0 if you lost, 3 if the round was a draw, and 6 if you won)
# "Anyway, the second column says how the round needs to end:
# X means you need to lose, Y means you need to end the round in a draw, and Z means you need to win. Good luck!"

win_lose_draw = {"X": 0, "Y": 3, "Z": 6}
need_to_throw = {"A X": 3, "A Y": 1, "A Z": 2, "B X": 1, "B Y": 2, "B Z": 3,
                 "C X": 2, "C Y": 3, "C Z": 1}

with open("day_2_1.txt") as f:
    array = [line.rstrip() for line in f]

my_score = 0
for i in array:
    my_score = need_to_throw[i] + my_score + win_lose_draw[i[-1:]] # score to add for my win

print(f"my score at rock paper scissors is", my_score)
