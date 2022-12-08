# Advent of code 6.2
# Happy Advent!

# Your device's communication system is correctly detecting packets, but still isn't working.  It looks like it also
# needs to look for messages.  A start-of-message marker is just like a start-of-packet marker, except it consists of
# 14 distinct characters rather than 4.
# How many characters need to be processed before the first start-of-message marker is detected?

with open("day_6_1.txt") as f:
    array = [line.rstrip() for line in f]
input = array[0]

for i in range(0, len(input)):
    unique_chars = ''.join(set(input[i:i+14]))
    if len(unique_chars)==14:
        print(f"Signal processed.  the message synchronization number is", i+14)
        break
