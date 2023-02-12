import re
from itertools import permutations

with open("2015/input_13.txt", "r") as f:
    instructions = [i[:-1] for i in f.readlines()]

rgx = re.compile(r"(.+) would (.+) (\d+) happiness units by sitting next to (.+).")

gain = {}

for i in instructions:
    who, what, n, where = rgx.search(i).groups()
    if who not in gain:
        gain[who] = {}
    n = -int(n) if what == "lose" else int(n)
    gain[who][where] = n

people = list(gain.keys())
happiness = 0

for i in permutations(people):
    h = 0
    h += gain[i[0]][i[-1]] + gain[i[0]][i[1]]
    for j in range(1, len(i) - 1):
        h += gain[i[j]][i[j - 1]] + gain[i[j]][i[j + 1]]
    h += gain[i[-1]][i[-2]] + gain[i[-1]][i[0]]

    happiness = max(happiness, h)

# ANSWER 1
print(happiness)

for i in gain:
    gain[i]["me"] = 0
gain["me"] = {}
for p in people:
    gain["me"][p] = 0

people.append("me")

happiness = 0

for i in permutations(people):
    h = 0
    h += gain[i[0]][i[-1]] + gain[i[0]][i[1]]
    for j in range(1, len(i) - 1):
        h += gain[i[j]][i[j - 1]] + gain[i[j]][i[j + 1]]
    h += gain[i[-1]][i[-2]] + gain[i[-1]][i[0]]

    happiness = max(happiness, h)

# ANSWER 2
print(happiness)

# probably not the smartest, but is "fast enough" and works, yay brute force
# instead of adding me and iterating through all permutations again,
# faster would probably be figuring out the lowest happiness pair in the seating and adding me between those

# a tiny possible speed-up, found on reddit (u/fiavolo):
# "Since the table is circular, I can keep the first person in the same spot
# and only permute the order of people who come after."
