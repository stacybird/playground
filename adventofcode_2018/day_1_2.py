# Advent of code 1.2
# Happy Advent!
with open("day_1_1.txt") as f:
    num_array = [int(line.rstrip()) for line in f]
seen_sums = []
sum = 0
flag = False
while True:
    for element in num_array:
        sum += element
        if sum in seen_sums:
            flag = True
            break
        seen_sums.append(sum)
    if flag is True:
        break

print(sum)
