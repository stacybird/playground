# Advent of code 2.1
# Happy Advent!
#                "The first column is what your opponent is going to play: A for Rock, B for Paper, and C for Scissors."
# The second column, you reason, must be what you should play in response: X for Rock, Y for Paper, and Z for Scissors.
# The score for a single round is the score for the shape you selected (1 for Rock, 2 for Paper, and 3 for Scissors)
# plus the score for the outcome of the round (0 if you lost, 3 if the round was a draw, and 6 if you won)

shape_scores = {"X": 1, "Y": 2, "Z": 3}
win_scores = {"A X": 3, "A Y": 6, "A Z": 0, "B X": 0, "B Y": 3, "B Z": 6, "C X": 6, "C Y": 0, "C Z": 3}

with open("day_2_1.txt") as f:
    array = [line.rstrip() for line in f]

my_score = 0
for i in array:
    my_score = win_scores[i] + my_score + shape_scores[i[-1:]]

print(f"my score at rock paper scissors is", my_score)
