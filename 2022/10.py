with open("2022/input_10.txt", "r") as f:
    instructions = [i[:-1] for i in f.readlines()]

cycle = 0
X = 1
key_cycles = [20, 60, 100, 140, 180, 220]
strengths = []

for i in instructions:
    if i.startswith("noop"):
        cycle += 1
        if cycle == key_cycles[0]:
            strengths.append(X * key_cycles[0])
            key_cycles.pop(0)
    elif i.startswith("addx"):
        V = int(i.split(" ")[1])
        cycle += 2
        if cycle >= key_cycles[0]:
            strengths.append(X * key_cycles[0])
            key_cycles.pop(0)
        X += V
    if not key_cycles:
        break

# ANSWER 1
print(sum(strengths))

drawing = [" "] * 240

X = 1
position = 0

for i in instructions:
    if i.startswith("noop"):
        if abs(X - (position % 40)) <= 1:
            drawing[position] = "#"
        position += 1

    elif i.startswith("addx"):
        V = int(i.split(" ")[1])
        if abs(X - (position % 40)) <= 1:
            drawing[position] = "#"
        position += 1
        if abs(X - (position % 40)) <= 1:
            drawing[position] = "#"
        position += 1
        X += V


drawing = "".join(drawing)
# ANSWER 2
for i in range(6):
    print(drawing[40 * i : 40 * (i + 1)])
