# ok today i decided that i will attempt this year using standard library for as long as possible
import re

with open("2022/input_05.txt", "r") as f:
    instructions = [i[:-1] for i in f.readlines()]

# split instructions into the parts
for n, i in enumerate(instructions):
    if i == "":
        crates_list = instructions[: n - 1]
        n_crates = instructions[n - 1]
        procedures = instructions[n + 1 :]
        break

# initialize crates
n_crates = max([int(x) for x in n_crates.split(" ") if not x in [" ", ""]])
crates = [[] for i in range(n_crates)]

# fill crates with starting positions
re_crates = re.compile(r"[ \[\]]")
for i in range(len(crates_list) - 1, -1, -1):
    crate_row = crates_list[i] + " "
    for i in range(0, len(crate_row), 4):
        c = crate_row[i : i + 4]
        c = re_crates.sub("", c)
        if c != "":
            crates[i // 4].append(c)

# run procedures
for i in procedures:
    n, from_crate, to_crate = re.match(r"move (\d+) from (\d+) to (\d+)", i).groups()
    n = int(n)
    from_crate = int(from_crate) - 1
    to_crate = int(to_crate) - 1

    for j in range(n):
        moving = crates[from_crate].pop()
        crates[to_crate].append(moving)

# ANSWER 1
print("".join([x[-1] for x in crates]))

crates_2 = [[] for i in range(n_crates)]

# fill crates with starting positions
for i in range(len(crates_list) - 1, -1, -1):
    crate_row = crates_list[i] + " "
    for i in range(0, len(crate_row), 4):
        c = crate_row[i : i + 4]
        c = re_crates.sub("", c)
        if c != "":
            crates_2[i // 4].append(c)

# run procedures

for i in procedures:
    n, from_crate, to_crate = re.match(r"move (\d+) from (\d+) to (\d+)", i).groups()
    n = int(n)
    from_crate = int(from_crate) - 1
    to_crate = int(to_crate) - 1

    moving = crates_2[from_crate][-n:]
    del crates_2[from_crate][-n:]
    crates_2[to_crate].extend(moving)

# ANSWER 2
print("".join([x[-1] for x in crates_2]))
