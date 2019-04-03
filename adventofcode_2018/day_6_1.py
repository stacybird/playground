# Advent of code 6.1
# Happy Advent!

import re

with open("day_6.txt") as f:
    num_list = [list(map(int, re.findall(r'\d+', line.rstrip()))) for line in f]

grid = [['.' for i in range(360)] for j in range(360)]

flag = False
letter = 'A'
points = {}
for x,y in num_list:
    if flag:
        grid[x][y] = letter + letter
        points[letter + letter] = (x, y)
    else:
        grid[x][y] = letter
        points[letter] = (x, y)
    if letter == 'Z':
        letter = 'A'
        flag = True
    else:
        letter = chr(ord(letter) +1)


def set_value():
    if (0 < x < 360) and (0 < y < 360):
        if grid[x][y] == '.':
            grid[x][y] = lower_k
        else:
            grid[x][y] = '?'


for i in range(1, 360):
    for key in points:
        lower_k = key.lower()
        a, b = points[key]
        x = a+i
        y = b
        if x < 360:
            while x != a:
                set_value()
                y = y+1
                x = x-1
        if y < 360:
            while y != b:
                set_value()
                x = x-1
                y = y-1
        if x >= 0:
            set_value()
        if y >=0:
            set_value()

for i in range(0,360):
     print(grid[i])
#
# print(num_list.__len__())
# print(points)
