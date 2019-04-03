# Advent of code 6.1
# Happy Advent!

import re

with open("day_6.txt") as f:
    num_list = [list(map(int, re.findall(r'\d+', line.rstrip()))) for line in f]

grid = [[0 for i in range(360)] for j in range(360)]


for x,y in num_list:
    grid[x][y] = "."
    print(x,y)

for i in range(50,57):
    print(grid[i])
