# Advent of code 3.2
# Happy Advent!

import re

# format:           #claim_id @ left_offset,top_offset: width,height
# eg:               #302 @ 498,651: 15x24
# is converted to   [302, 498, 651, 15, 24]
with open("day_3_1.txt") as f:
    num_list = [list(map(int, re.findall(r'\d+', line))) for line in f]

# initialize cloth
cloth = [[0 for i in range(1000)] for j in range(1000)]

# populate cloth table
for row in num_list:
    # left_offset, left_offset + width
    for j in range(row[1], row[1] + row[3]):
        # top_offset, top_offset + height
        for i in range(row[2], row[2] + row[4]):
            cloth[i][j] += 1

cloth_swatch = []
# check for a swatch without overlap
for row in num_list:
    row_failed = False
    for j in range(row[1], row[1] + row[3]):
        for i in range(row[2], row[2] + row[4]):
            if cloth[i][j] > 1:
                row_failed = True
    if row_failed == False:
        cloth_swatch = row
        break

print("swatch id", cloth_swatch[0], "doesn't overlap any other")
