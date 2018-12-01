# Advent of code 1.1
# Happy Advent!
with open("day_1_1.txt") as f:
    num_array = [int(line.rstrip()) for line in f]
array_sum = sum(num_array)
print(array_sum)
