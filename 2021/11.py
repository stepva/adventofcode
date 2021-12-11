# %%
import numpy as np

f = open("2021/input_11.txt", "r")
lines = f.readlines()

# %%
a = np.empty((0, 10))
for l in lines:
    l = l[:-1]
    a = np.vstack([a, list(l)]).astype(int)

#%%
def check_flash(a):
    w = np.where(a == 10)
    xs, ys = w[0], w[1]
    for i in range(0, len(xs)):
        flash(a, xs[i], ys[i])

    if np.where(a == 10)[0].size != 0:
        check_flash(a)

    a[np.where(a > 9)] = 0


# %%
def flash(a, x, y):
    x1 = max(0, x - 1)
    b = 2 if x == 0 else 3
    x2 = min(10, x1 + b)
    y1 = max(0, y - 1)
    b = 2 if y == 0 else 3
    y2 = min(10, y1 + b)

    arr = a[x1:x2, y1:y2]
    arr += 1
    arr[arr == 11] = 10
    a[x, y] = 11


# %%
flashes = 0
for i in range(0, 100):
    a = a + 1
    check_flash(a)
    flashes += sum(sum(a == 0))

# %%
# ANSWER 1
print(flashes)

# %%
a = np.empty((0, 10))
for l in lines:
    l = l[:-1]
    a = np.vstack([a, list(l)]).astype(int)

i = 0
while sum(sum(a == 0)) != 100:
    i += 1
    a = a + 1
    check_flash(a)

# %%
# ANSWER 2
print(i)
