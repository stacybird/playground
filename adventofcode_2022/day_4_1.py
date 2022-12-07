# Advent of code 4.1
# Happy Advent!

# However, as some of the Elves compare their section assignments with each other, they've noticed that many
# of the assignments overlap.  In how many assignment pairs does one range fully contain the other?


with open("day_4_1.txt") as f:
    array = [line.rstrip() for line in f]
count_containing_sets = 0

for i in array:
    a, b = i.split(",")
    list_1 = [*range(int(a.split("-")[0]),
                     int(a.split("-")[1]) + 1, 1)]
    list_2 = [*range(int(b.split("-")[0]),
                     int(b.split("-")[1]) + 1, 1)]
    if (all(x in list_1 for x in list_2)):
        count_containing_sets += 1
    else:
        if (all(x in list_2 for x in list_1)):
            count_containing_sets += 1

print(f"Count of workorder pair ranges containing each other", count_containing_sets)
