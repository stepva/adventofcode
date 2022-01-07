# %%
from collections import Counter

# %%
f = open("input_14.txt", "r")
lines = f.readlines()

template = lines[0][:-1]
rules = {}
for l in lines[2:]:
    l = l[:-1]
    lsplit = l.split(" -> ")
    rules[lsplit[0]] = lsplit[1]

# %%
for i in range(0, 10):
    next_temp = ""
    for i in range(0, len(template) - 1):
        next_temp += template[i]
        pair = template[i : i + 2]
        next_temp += rules[pair]
    next_temp += template[-1]
    template = next_temp

# %%
polycount = Counter(template)
# ANSWER 1
print(
    polycount[max(polycount, key=polycount.get)]
    - polycount[min(polycount, key=polycount.get)]
)

# %%
template = lines[0][:-1]
pairs = []
for i in range(0, len(template) - 1):
    pairs.append(template[i : i + 2])

# %%
def polymer(pairs, total, n):
    new_pairs = []
    for p in pairs:
        for i in range(0, n):
            next_temp = ""
            for i in range(0, len(p) - 1):
                next_temp += p[i]
                pair = p[i : i + 2]
                next_temp += rules[pair]
            next_temp += p[-1]
            p = next_temp

        p_pairs = []
        for i in range(0, len(p) - 1):
            pairs.append(p[i : i + 2])
        new_pairs.append(p_pairs)

        polycount = Counter(p[:-1])
        for c in polycount:
            total[c] = total.get(c, 0) + polycount[c]

    return total, new_pairs


# %%
total = {}
total, new_pairs = polymer(pairs, total, 10)

# %%
polycount = Counter(total)
print(
    polycount[max(polycount, key=polycount.get)]
    - polycount[min(polycount, key=polycount.get)]
)

# %%
total = {}
for p in pairs:
    for i in range(0, 10):
        next_temp = ""
        for i in range(0, len(p) - 1):
            next_temp += p[i]
            pair = p[i : i + 2]
            next_temp += rules[pair]
        next_temp += p[-1]
        p = next_temp
    polycount = Counter(p[:-1])
    for c in polycount:
        total[c] = total.get(c, 0) + polycount[c]

last = pairs[-1][-1]
total[last] += 1
# %%
polycount = Counter(total)
print(
    polycount[max(polycount, key=polycount.get)]
    - polycount[min(polycount, key=polycount.get)]
)

# %%
