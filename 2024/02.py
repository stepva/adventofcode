import copy

with open("2024/input_02.txt", "r") as f:
    instructions = [i[:-1] for i in f.readlines()]

safe = 0


def is_safe(level):
    base = level[1] - level[0]
    if not 1 <= abs(base) <= 3:
        return False
    
    for l in range(2, len(level)):
        dist = level[l] - level[l-1]
        if (dist - abs(dist) == 0) != (base - abs(base) == 0):
            return False
        if not 1 <= abs(dist) <= 3:
            return False
        
    return True

for i in instructions:
    level = i.split(" ")
    level = [int(l) for l in level]
    if is_safe(level):
        safe += 1

# ANSWER 1
print(safe)

safe = 0

for i in instructions:
    level = i.split(" ")
    level = [int(l) for l in level]
    if is_safe(level):
        safe += 1
    else:
        for l in range(len(level)):
            levelcopy = copy.deepcopy(level)
            levelcopy.pop(l)
            if is_safe(levelcopy):
                safe += 1
                break

# ANSWER 2
print(safe)

        



