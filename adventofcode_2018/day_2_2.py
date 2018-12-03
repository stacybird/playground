# Advent of code 2.2
# Happy Advent!
with open("day_2_1.txt") as f:
    string_array = [line.rstrip() for line in f]

temporary_match = ""
matching_box_chars = ""

def compare(e1, e2):
    new_string = ""
    for char1, char2 in zip(e1, e2):
        if char1 == char2:
            new_string += char1
    return new_string

for element in string_array:
    for e3 in string_array:
        if element == e3:
            pass
        else:
            temporary_match = compare(element, e3)
            if len(temporary_match) > len(matching_box_chars):
                matching_box_chars = temporary_match

print(matching_box_chars)