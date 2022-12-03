with open("2022/input_03.txt", "r") as f:
    instructions = [i[:-1] for i in f.readlines()]


def get_priority(ch: str) -> int:
    if ch == ch.upper():
        return ord(ch) - 38
    else:
        return ord(ch) - 96


priority = 0
for i in instructions:
    half = int(len(i) / 2)
    first = set(i[:half])
    second = set(i[half:])
    common = first.intersection(second).pop()
    priority += get_priority(common)

# ANSWER 1
print(priority)

badge_priority = 0
for i in range(0, len(instructions), 3):
    group = instructions[i : i + 3]
    common = set(group[0]).intersection(set(group[1])).intersection(set(group[2])).pop()
    badge_priority += get_priority(common)

# ANSWER 2
print(badge_priority)
