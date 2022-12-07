# Advent of code 3.2
# Happy Advent!

# For efficiency, within each group of three Elves, the badge is the only item type carried by all three Elves.
# That is, if a group's badge is item type B, then all three Elves will have item type B somewhere in their rucksack,
# and at most two of the Elves will be carrying any other item type.
# Priorities for these items must still be found to organize the sticker attachment efforts.  Find the item type
# that corresponds to the badges of each three-Elf group. What is the sum of the priorities of those item types?

with open("day_3_1.txt") as f:
    array = [line.rstrip() for line in f]
groups_of_three = [array[i:i + 3] for i in range(0, len(array), 3)]
my_priority_sum = 0

for i in groups_of_three:
    common_character = ''.join(
        set([char for char in i[0] if char in
             (char for char in i[1] if char in i[2])]))
    if common_character.isupper():
        my_priority_sum = my_priority_sum + ord(common_character) - 38
    else:
        my_priority_sum = my_priority_sum + ord(common_character) - 96

print(f"Sum of item types priority is", my_priority_sum)
