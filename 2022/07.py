import re

with open("2022/input_07.txt", "r") as f:
    instructions = [i[:-1] for i in f.readlines()]

dirs = {}
visits = []
re_cd = re.compile(r"^\$ cd (.+)$")
re_file = re.compile(r"^(\d+) (.+)$")

for i in instructions:
    if i.startswith("dir") or i == "$ ls":
        # see note below
        continue

    cd = re_cd.search(i)
    if cd:
        cd = cd.group(1)
        if cd == "..":
            visits.pop()
        else:
            visits.append(cd)
            path = "/".join(visits)
            if path not in dirs:
                dirs[path] = 0
        if cd == "/":
            visits = visits[0:]
        continue

    f = re_file.search(i)
    if f:
        size = int(f.group(1))
        for vi in range(0, len(visits)):
            path = "/".join(visits[: vi + 1])
            dirs[path] += size

# I am aware that my solution does not check for the case when $ ls is called for the second time in one directory
# which would then result in adding the file sizes again, but that case is not present in my input (ie. probably in no input either)
# and I don't have the time and motivation to include it in my solution now, sorry

# ANSWER 1
print(sum([x for x in dirs.values() if x <= 100000]))

disk_space = 70000000
free = disk_space - dirs["/"]
need = 30000000 - free

sizes = [x for x in dirs.values() if x > need]

# ANSWER 2
print(min(sizes))
