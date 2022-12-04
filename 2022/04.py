with open("2022/input_04.txt", "r") as f:
    instructions = [i[:-1] for i in f.readlines()]

count = 0

for i in instructions:
    first, second = i.split(",")
    first = [int(x) for x in first.split("-")]
    second = [int(x) for x in second.split("-")]

    if first[0] >= second[0] and first[1] <= second[1]:
        count += 1
    elif first[0] <= second[0] and first[1] >= second[1]:
        count += 1

# ANSWER 1
print(count)

overlaps = 0

for i in instructions:
    first, second = i.split(",")
    first = [int(x) for x in first.split("-")]
    second = [int(x) for x in second.split("-")]

    if first[1] >= second[0] and first[0] <= second[0]:
        overlaps += 1
    elif second[1] >= first[0] and second[0] <= first[0]:
        overlaps += 1

# ANSWER 2
print(overlaps)
