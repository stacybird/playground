# Advent of code 4.2
# Happy Advent!

import re

# time range to cover: 00:00 - 00:59

with open("day_4.txt") as f:
    string_list = [line.rstrip() for line in f]

sorted_list = sorted(string_list)
guards = {}

for string in sorted_list:
    if string.__contains__("Guard"):
        guard_id = re.findall(r'\d+', string)[-1]
        if guard_id not in guards:
            guards[guard_id] = [0 for i in range(60)]
    else:
        current_time = int(re.findall(r'\d+', string)[-1])
        if string.__contains__("falls asleep"):
            asleep_time = current_time
        else:
            for i in range(asleep_time, current_time):
                guards[guard_id][i] += 1

guard_max = {}
for guard_id in guards:
    guard_max[guard_id] = max(guards[guard_id])

frequently_sleepy_guard = max(guard_max, key=guard_max.get)
best_minute = guards[frequently_sleepy_guard].index(guard_max[frequently_sleepy_guard])

print("frequently sleepy guard", frequently_sleepy_guard)
print("best minute", best_minute)
print(int(frequently_sleepy_guard) * best_minute)
