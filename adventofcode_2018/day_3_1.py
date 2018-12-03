# Advent of code 3.1
# Happy Advent!

import re

# format
# #claim_id @ left_offset,top_offset: width,height
# eg:  #302 @ 498,651: 15x24
# is converted to  [302, 498, 651, 15, 24]
with open("day_3_1.txt") as f:
    num_list = [list(map(int, re.findall(r'\d+', line.rstrip()))) for line in f]

# initialize cloth
cloth = [[0 for i in range(1000)] for j in range(1000)]

# populate cloth table
for row in num_list:
    # left_offset, left_offset + width
    for j in range(row[1], row[1] + row[3]):
        # top_offset, top_offset + height
        for i in range(row[2], row[2] + row[4]):
            cloth[i][j] += 1

counter = 0
# How many square inches of fabric are within two or more claims?
for i in range(1000):
    for j in range(1000):
        if cloth[i][j] >= 2:
            counter += 1

print(counter, "square inches with two or more claims")
