# Advent of code 5.2
# Happy Advent!

with open("day_5.txt") as f:
    my_input = [line.rstrip() for line in f][0]

alphabet = 'abcdefghijklmnopqrstuvwxyz'
removed_unit_list_lengths = []
min_value = 50000


def remove_dupes(my_string):
    for c in my_string:
        if c.islower():
            my_string = my_string.replace(c + c.upper(), '')
        else:
            my_string = my_string.replace(c + c.lower(), '')
    return my_string


for char in alphabet:
    output = my_input.replace(char.upper(), '').replace(char, '')
    previous_len = 0
    while True:
        output = remove_dupes(output)
        current_len = len(output)
        if current_len == previous_len:
            break
        previous_len = current_len
    removed_unit_list_lengths.append(len(output))

print("Minimum length output with an element removed:", min(removed_unit_list_lengths))
