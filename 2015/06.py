import numpy as np

f = open("2015/input_6.txt", "r")
instructions = f.readlines()

grid = np.zeros((1000, 1000))

for i in instructions:
    i = i[:-1]
    splits = i.split(" ")
    x1, y1 = int(splits[-3].split(",")[0]), int(splits[-3].split(",")[1])
    x2, y2 = int(splits[-1].split(",")[0]), int(splits[-1].split(",")[1])

    x = x2 - x1 + 1
    y = y2 - y1 + 1
    count = x * y

    if splits[1] == "on":
        for i in range(x1, x2 + 1):
            for ii in range(y1, y2 + 1):
                grid[i][ii] = 1
    elif splits[1] == "off":
        for i in range(x1, x2 + 1):
            for ii in range(y1, y2 + 1):
                grid[i][ii] = 0
    else:
        for i in range(x1, x2 + 1):
            for ii in range(y1, y2 + 1):
                if grid[i][ii] == 0:
                    grid[i][ii] = 1
                elif grid[i][ii] == 1:
                    grid[i][ii] = 0

on = grid.sum()
# ANSWER 1
print(on)

grid = np.zeros((1000, 1000))

for i in instructions:
    i = i[:-1]
    splits = i.split(" ")
    x1, y1 = int(splits[-3].split(",")[0]), int(splits[-3].split(",")[1])
    x2, y2 = int(splits[-1].split(",")[0]), int(splits[-1].split(",")[1])

    x = x2 - x1 + 1
    y = y2 - y1 + 1
    count = x * y

    if splits[1] == "on":
        for i in range(x1, x2 + 1):
            for ii in range(y1, y2 + 1):
                grid[i][ii] += 1
    elif splits[1] == "off":
        for i in range(x1, x2 + 1):
            for ii in range(y1, y2 + 1):
                grid[i][ii] = max(grid[i][ii] - 1, 0)
    else:
        for i in range(x1, x2 + 1):
            for ii in range(y1, y2 + 1):
                grid[i][ii] += 2

on = grid.sum()
# ANSWER 2
print(on)
