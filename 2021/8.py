#%%
from collections import Counter

#%%
f = open("2021/input_8.txt", "r")

lines = f.readlines()

#%%
alls = []
digs = []
for l in lines:
    lines_digs = l[:-1].split(" | ")
    alls.append(lines_digs[0].split(" "))
    digs.append(lines_digs[1].split(" "))

# %%
digs_right = [d for dl in digs for d in dl]
digs_lens = list(map(lambda x: len(x), digs_right))
digs_count = Counter(digs_lens)

# %%
# ANSWER 1
print(digs_count[2] + digs_count[3] + digs_count[4] + digs_count[7])

# %%
total = 0
for r in range(0, len(alls)):
    lends = {2: [], 3: [], 4: [], 5: [], 6: [], 7: []}
    for d in alls[r]:
        lends[len(d)].append(d)

    top = [ch for ch in lends[3][0] if ch not in lends[2][0]][0]
    horiz = [ch for ch in lends[5][0] if ch in lends[5][1] and ch in lends[5][2]]
    mid = [ch for ch in horiz if ch in lends[4][0]][0]
    bot = [ch for ch in horiz if ch != top and ch != mid][0]
    top_left = [ch for ch in lends[4][0] if ch != mid and ch not in lends[2][0]][0]
    five = [w for w in lends[5] if top_left in w][0]
    bot_right = [ch for ch in five if ch not in horiz + [top_left]][0]
    top_right = [ch for ch in lends[2][0] if ch != bot_right][0]
    nine = [w for w in lends[6] if all(x in list(five + top_right) for x in list(w))][0]
    bot_left = [ch for ch in list(lends[7][0]) if ch not in list(nine)][0]

    zero = [ch for ch in lends[7][0] if ch != mid]
    one = list(lends[2][0])
    two = [ch for ch in lends[7][0] if ch != top_left and ch != bot_right]
    three = [ch for ch in lends[7][0] if ch != top_left and ch != bot_left]
    four = list(lends[4][0])
    five = list(five)
    six = [ch for ch in lends[7][0] if ch != top_right]
    seven = list(lends[3][0])
    eight = list(lends[7][0])
    nine = list(nine)

    value = ""
    for d in digs[r]:
        dset = set(list(d))
        if dset == set(zero):
            value += "0"
        elif dset == set(one):
            value += "1"
        elif dset == set(two):
            value += "2"
        elif dset == set(three):
            value += "3"
        elif dset == set(four):
            value += "4"
        elif dset == set(five):
            value += "5"
        elif dset == set(six):
            value += "6"
        elif dset == set(seven):
            value += "7"
        elif dset == set(eight):
            value += "8"
        elif dset == set(nine):
            value += "9"

    total += int(value)

# %%
# ANSWER 2
print(total)
