# Advent of code 1.1
# Happy Advent!
with open("day_1_1.txt") as f:
    array = [line.rstrip() for line in f]
j = 0
array_sums = [0]
array_sums[j] = 0
for i in array:
    if i == '':
        j = j + 1
        array_sums.insert(j,0)
    else:
        array_sums[j] = array_sums[j] + int(i)
print("this elf is carrying the most calories:")
print(array_sums.index(max(array_sums))+1)
