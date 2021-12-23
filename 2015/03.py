f = open("2015/input_3.txt", "r")
inputs = f.readlines()[0]

santa = inputs[::2]
robo = inputs[1::2]

x = 0
y = 0
houses = [(x, y)]

for i in inputs:
    if i == ">":
        x += 1
    elif i == "<":
        x -= 1
    elif i == "^":
        y += 1
    elif i == "v":
        y -= 1
    houses.append((x, y))

uniques = list(set(houses))
# ANSWER 1
print(len(uniques))

s_uniq = []
for s in [santa, robo]:
    x = 0
    y = 0
    houses = [(x, y)]
    for i in s:
        if i == ">":
            x += 1
        elif i == "<":
            x -= 1
        elif i == "^":
            y += 1
        elif i == "v":
            y -= 1
        houses.append((x, y))
    uniques = list(set(houses))
    s_uniq.append(uniques)

uniques_2 = list(set(s_uniq[0] + s_uniq[1]))
# ANSWER 2
print(len(uniques_2))
