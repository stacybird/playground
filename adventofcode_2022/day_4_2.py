# Advent of code 4.2
# Happy Advent!

# However, as some of the Elves compare their section assignments with each other, they've noticed that many
# of the assignments overlap.  In how many assignment pairs do the ranges overlap?

with open("day_4_1.txt") as f:
    array = [line.rstrip() for line in f]
count_overlapping_sets = 0

for i in array:
    a, b = i.split(",")
    x = range(int(a.split("-")[0]),
              int(a.split("-")[1]) + 1, 1)
    y = range(int(b.split("-")[0]),
              int(b.split("-")[1]) + 1, 1)
    if (range(max(x[0], y[0]), min(x[-1], y[-1]) + 1)) != range(0):
        count_overlapping_sets += 1

print(f"Count of workorder pair ranges overlapping", count_overlapping_sets)
