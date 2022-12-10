# Advent of code 7.1
# Happy Advent!

# Find all of the directories with a total size of at most 100,000.
# What is the sum of the total sizes of those directories?
# import json

with open("day_7_1.txt") as f:
    array = [line.rstrip() for line in f]

dir_listing = {}
cwd = ""
lower_dir_count = 0

for i in array:
    if " .." in i:
        lower_dir_count = dir_listing[cwd]
        cwd = "$".join(cwd.split("$")[:-1])
        dir_listing[cwd] += lower_dir_count
    else:
        if "cd " in i:
            cwd = cwd + "$" + i.split()[-1]
            dir_listing[cwd] = 0

        else:
            if any(char.isdigit() for char in i):
                dir_listing[cwd] = dir_listing[cwd] + int(i.split()[0])

my_sum = 0
for value in dir_listing.values():
    if value < 100000:
        my_sum += value

print("the sum of dirs less than 100000 each is: ", my_sum)
