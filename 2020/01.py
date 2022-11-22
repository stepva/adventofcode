import numpy as np

instructions = np.loadtxt("2020/input_01.txt")

smaller = []
larger = []
for i in instructions:
    if i < 1010:
        smaller.append(i)
    else:
        larger.append(i)

for i in smaller:
    for j in larger:
        if i + j == 2020:
            # ANSWER 1
            print(i * j)
            break
    else:
        continue
    break

for i in range(len(instructions) - 2):
    for j in range(i + 1, len(instructions) - 1):
        for k in range(j + 1, len(instructions)):
            # can use np.sum(instructions[[i, j, k]]) (also np.prod(instructions[[i, j, k]])) but it's a lot slower lol
            if instructions[i] + instructions[j] + instructions[k] == 2020:
                # ANSWER 2
                print(instructions[i] * instructions[j] * instructions[k])
                break
        else:
            continue
        break
    else:
        continue
    break
