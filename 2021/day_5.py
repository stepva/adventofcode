# %%
import numpy as np

f = open("2021/input_5.txt", "r")
lines = f.readlines()
m = np.zeros((1000, 1000))

# %%
for l in lines:
    l = l[:-1].split(" -> ")
    x1, y1 = l[0].split(",")
    x2, y2 = l[1].split(",")
    x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
    if (x1 == x2) or (y1 == y2):
        for x in range(min(x1, x2), max(x2, x1) + 1):
            for y in range(min(y1, y2), max(y2, y1) + 1):
                m[y][x] += 1

# %%
# ANSWER 1
print(len(np.where(m > 1)[0]))

# %%
m2 = np.zeros((1000, 1000))

for l in lines:
    l = l[:-1].split(" -> ")
    x1, y1 = l[0].split(",")
    x2, y2 = l[1].split(",")
    x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
    if (x1 == x2) or (y1 == y2):
        for x in range(min(x1, x2), max(x2, x1) + 1):
            for y in range(min(y1, y2), max(y2, y1) + 1):
                m2[y][x] += 1
    else:
        xs, ys = [], []
        xi = 1 if x2 > x1 else -1
        yi = 1 if y2 > y1 else -1
        for x in range(x1, x2 + xi, xi):
            xs.append(x)
        for y in range(y1, y2 + yi, yi):
            ys.append(y)
        for n in range(0, len(xs)):
            m2[ys[n]][xs[n]] += 1

# %%
# ANSWER 2
print(len(np.where(m2 > 1)[0]))
