# Advent of code 5.1
# Happy Advent!

with open("day_5.txt") as f:
    input = [line.rstrip() for line in f][0]

for char in input:
    if char.islower():
        input = input.replace(char + char.upper(), '')
    else:
        input = input.replace(char + char.lower(), '')

print('There are', len(input), 'unique units')
