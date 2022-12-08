# Advent of code 6.1
# Happy Advent!

# To fix the communication system, you need to add a subroutine to the device that detects a start-of-packet marker
# in the datastream. In the protocol being used by the Elves, the start of a packet is indicated by a sequence of
# four characters that are all different.
# How many characters need to be processed before the first start-of-packet marker is detected?

with open("day_6_1.txt") as f:
    array = [line.rstrip() for line in f]
input = array[0]

for i in range(0, len(input)):
    unique_chars = ''.join(set(input[i:i+4]))
    if len(unique_chars)==4:
        print(f"Signal processed.  the signal synchronization number is", i+4)
        break
