# Advent of code 2.1
# Happy Advent!
with open("day_2_1.txt") as f:
    string_array = [line.rstrip() for line in f]
two_times = 0
three_times = 0


def has_two(e):
    for char in e:
        if e.count(char) == 2:
            return 1
    return 0

def has_three(e):
    for char in e:
        if e.count(char) == 3:
            return 1
    return 0

for element in string_array:
    two_times += has_two(element)
    three_times += has_three(element)

checksum = two_times * three_times

print(two_times, "*", three_times, "=", checksum)
