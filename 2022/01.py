f = open("2022/input_01.txt", "r")
instructions = f.readlines()
instructions = [i[:-1] for i in instructions]

max_calories = 0
current_elf = 0

for i in instructions:
    if i == "":
        max_calories = max(max_calories, current_elf)
        current_elf = 0
    else:
        current_elf += int(i)

# ANSWER 1
print(max_calories)

calories = []
current_elf = 0

for i in instructions:
    if i == "":
        calories.append(current_elf)
        current_elf = 0
    else:
        current_elf += int(i)

# ANSWER 2
print(sum(sorted(calories, reverse=True)[:3]))
