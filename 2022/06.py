with open("2022/input_06.txt", "r") as f:
    instructions = [i[:-1] for i in f.readlines()][0]

for i in range(len(instructions) - 4):
    marker = instructions[i : i + 4]
    if len(set(marker)) == 4:
        # ANSWER 1
        print(i + 4)
        break

for i in range(len(instructions) - 14):
    marker = instructions[i : i + 14]
    if len(set(marker)) == 14:
        # ANSWER 2
        print(i + 14)
        break
