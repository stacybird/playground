# Advent of code 4.1
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

guard_sums = {}
for guard_id in guards:
    guard_sums[guard_id] = sum(guards[guard_id])

sleepy_guard = max(guard_sums, key=guard_sums.get)
best_minute = guards[sleepy_guard].index(max(guards[sleepy_guard]))

print("sleepy guard", sleepy_guard)
print("best minute", best_minute)
print(int(sleepy_guard) * best_minute)
