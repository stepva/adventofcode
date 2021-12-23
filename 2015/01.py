# %%
f = open("2015/input_1.txt", "r")
instructions = f.readlines()[0]

# %%
floor = 0
position = 1

for i in instructions:
    if i == "(":
        floor += 1
    elif i == ")":
        floor -= 1

# %%
# ANSWER 1
print(floor)

# %%
floor = 0
position = 1

for i in instructions:
    if i == "(":
        floor += 1
    elif i == ")":
        floor -= 1
    if floor != -1:
        position += 1
    elif floor == -1:
        break

# %%
# ANSWER 2
print(position)
