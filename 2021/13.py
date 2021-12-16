# %%
import numpy as np

f = open("2021/input_13.txt", "r")
lines = f.readlines()

nums, instructions = [], []
max_x = 0
max_y = 0
for l in lines:
    l = l[:-1]
    if l.startswith("fold"):
        instructions.append(l)
    else:
        if l != "":
            lsplit = l.split(",")
            max_y = max(max_y, int(lsplit[0]))
            max_x = max(max_x, int(lsplit[1]))
            nums.append([int(lsplit[1]), int(lsplit[0])])

#%%
a = np.zeros((max_x + 1, max_y + 1))
for n in nums:
    a[n[0]][n[1]] = 1

# %%
for n, i in enumerate(instructions):
    isplit = i.split(" ")[-1].split("=")
    line = isplit[0]
    num = int(isplit[1])

    if line == "x":
        a = a.transpose()

    a_1 = a[:][:num]
    a_2 = a[:][num + 1 :]
    a = a_1 + np.flipud(a_2)

    a[np.where(a > 1)] = 1

    if line == "x":
        a = np.rot90(a, 3)

    if n == 0:
        # ANSWER 1
        print(sum(sum(a)))

# %%
n = len(a[0]) / 8
a = a.transpose()
a[np.where(a == 0)] = np.nan

# %%
# ANSWER 2
for i in range(int(n), len(a) + 1, int(n)):
    letter = a[-int(n) :][:]
    a = a[: -int(n)][:]
    print(np.rot90(letter, 3), "\n")
