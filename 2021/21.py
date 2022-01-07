# %%
f = open("input_21.txt", "r")
lines = f.readlines()

space1 = int(lines[0][:-1][-1])
space2 = int(lines[1][:-1][-1])

# %%
score1 = 0
score2 = 0

d = 0
r = 0

# %%
while True:
    d1 = 100 if (d + 1) % 100 == 0 else (d + 1) % 100
    d2 = 100 if (d1 + 1) % 100 == 0 else (d1 + 1) % 100
    d3 = 100 if (d2 + 1) % 100 == 0 else (d2 + 1) % 100

    roll = d1 + d2 + d3
    d = d3
    r += 3

    space1 = 10 if (space1 + roll) % 10 == 0 else (space1 + roll) % 10
    score1 += space1

    if score1 >= 1000:
        break

    d1 = 100 if (d + 1) % 100 == 0 else (d + 1) % 100
    d2 = 100 if (d1 + 1) % 100 == 0 else (d1 + 1) % 100
    d3 = 100 if (d2 + 1) % 100 == 0 else (d2 + 1) % 100

    roll = d1 + d2 + d3
    d = d3
    r += 3

    space2 = 10 if (space2 + roll) % 10 == 0 else (space2 + roll) % 10
    score2 += space2

    if score2 >= 1000:
        break

#%%
# ANSWER 1
if score1 > score2:
    print(r * score2)
else:
    print(r * score1)

# %%

# %%
