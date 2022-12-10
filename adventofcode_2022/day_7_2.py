# Advent of code 7.2
# Happy Advent!

# Therefore, the update still requires a directory with total size of at least _____ to be deleted before it can run.
# Find the smallest directory that, if deleted, would free up enough space on the filesystem to run the update.
# What is the total size of that directory?

with open("day_7_1.txt") as f:
    array = [line.rstrip() for line in f]

dir_listing = {}
cwd = ""
lower_dir_count = 0

for i in array:
    if " .." in i:
        lower_dir_count = dir_listing[cwd]
        cwd = "$".join(cwd.split("$")[:-1])
        dir_listing[cwd] += lower_dir_count
    else:
        if "cd " in i:
            cwd = cwd + "$" + i.split()[-1]
            dir_listing[cwd] = 0

        else:
            if any(char.isdigit() for char in i):
                dir_listing[cwd] = dir_listing[cwd] + int(i.split()[0])

# disk_used = 42,388,255
# disk_free = 27,611,745
# update_size = 30,000,000
need_to_free = 2388255

my_values = []
# this was an odd answer - because of the files vs dirs.
# They asked for a dir, and the lowest is actually a file. semantics.
for value in dir_listing.values():
    if value >= need_to_free and value <= 2570000:
        my_values += [value]

print("values greater than 2,388,255: ", my_values)
