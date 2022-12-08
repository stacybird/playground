# Advent of code 5.1
# Happy Advent!

# The expedition can depart as soon as the final supplies have been unloaded from the ships.
# Supplies are stored in stacks of marked crates, but because the needed supplies are buried under many other crates,
# the crates need to be rearranged.
# They do, however, have a drawing of the starting stacks of crates and the rearrangement procedure (your puzzle input).
# After the rearrangement procedure completes, what crate ends up on top of each stack?

with open("day_5_1.txt") as f:
    array = [line.rstrip() for line in f]
count_overlapping_sets = 0
boxes = {1: "", 2: "", 3: "", 4: "", 5: "", 6: "", 7: "", 8: "", 9: ""}

print("initial box arrangement:")
for i in array:
    if not (any(char.isdigit() for char in i)):
        print(i)
        boxes[1] = i[1:2] + str(boxes[1])
        boxes[2] = i[5:6] + str(boxes[2])
        boxes[3] = i[9:10] + str(boxes[3])
        boxes[4] = i[13:14] + str(boxes[4])
        boxes[5] = i[17:18] + str(boxes[5])
        boxes[6] = i[21:22] + str(boxes[6])
        boxes[7] = i[25:26] + str(boxes[7])
        boxes[8] = i[29:30] + str(boxes[8])
        boxes[9] = i[33:34] + str(boxes[9])

        boxes = {
            key: value.replace(' ', '') for key, value in boxes.items()
        }
    if ("move" in i):

        k = i.split(" ")
        directions = {k[j]: int(k[j + 1]) for j in range(0, len(k), 2)}
        for k in range(0, directions["move"]):
            boxes[directions["to"]] = boxes[directions["to"]] + boxes[directions["from"]][-1:]
            boxes[directions["from"]] = boxes[directions["from"]][:-1]

print(f"Final box stacks.  bottom is left, right is top:", boxes)
