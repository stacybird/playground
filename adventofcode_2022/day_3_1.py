# Advent of code 3.1
# Happy Advent!

# Each rucksack has two large compartments. All items of a given type are meant to go into exactly one of the
# two compartments.  The list of items for each rucksack is given as characters all on a single line.
# A given rucksack always has the same number of items in each of its two compartments, so the
# first half of the characters represent items in the first compartment, while the second half of the characters
# represent items in the second compartment.
# Find the item type that appears in both compartments of each rucksack.
# What is the sum of the priorities of those item types?

with open("day_3_1.txt") as f:
    array = [line.rstrip() for line in f]

my_priority_sum = 0
for i in array:
    common_character = ''.join(
        set(
            [char for char in i[:len(i) // 2] if char in i[len(i) // 2:]]
        )
    )

    if common_character.isupper():
        my_priority_sum = my_priority_sum + ord(common_character) - 38
    else:
        my_priority_sum = my_priority_sum + ord(common_character) - 96

print(f"Sum of item types priority", my_priority_sum)
