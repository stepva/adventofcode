#%%
import numpy as np

f = open("2021/input_9.txt", "r")
lines = f.readlines()

# %%
a = np.array([])

for l in lines:
    l = l[:-1]
    l = [int(x) for x in list(l)]
    a = np.append(a, l)

# %%
risk = 0
for i in range(0, len(a)):
    cond = True
    if (i + 1) % 100 != 0:
        if a[i] >= a[i + 1]:
            cond = False
    if i != 0 and i % 100 != 0:
        if a[i] >= a[i - 1]:
            cond = False
    if i > 99:
        if a[i] >= a[i - 100]:
            cond = False
    if i < 9900:
        if a[i] >= a[i + 100]:
            cond = False

    if cond:
        risk += a[i] + 1

# %%
# ANSWER 1
print(risk)

#%%
def around(ones, a, i):
    r = 0
    if (i + 1) % 100 != 0:
        if ones[i + 1] == 1 or a[i + 1] == 9:
            r += 1
    if i != 0 and i % 100 != 0:
        if ones[i - 1] == 1 or a[i - 1] == 9:
            r += 1
    if i > 99:
        if ones[i - 100] == 1 or a[i - 100] == 9:
            r += 1
    if i < 9900:
        if ones[i + 100] == 1 or a[i + 100] == 9:
            r += 1

    if r < 4:
        return True
    else:
        return False


def check_adj(a, i, dir=["l", "r", "u", "d"]):
    if a[i] == 9 or ones[i] == 1:
        return 0

    if not around(ones, a, i):
        x = 0 if ones[i] == 1 else 1
        ones[i] = 1
        return x

    ones[i] = 1

    adj = 1

    if "r" in dir and (i + 1) % 100 != 0:
        adj += check_adj(a, i + 1, dir=["r", "u", "d"])
    if "l" in dir and i % 100 != 0:
        adj += check_adj(a, i - 1, dir=["l", "u", "d"])
    if "u" in dir and i > 99:
        adj += check_adj(a, i - 100, dir=["l", "r", "u"])
    if "d" in dir and i < 9900:
        adj += check_adj(a, i + 100, dir=["l", "r", "d"])

    return adj


# %%
ones = np.zeros(len(a))
b = np.array([])
for i in range(0, len(a)):
    if ones[i] == 1:
        b = np.append(b, 0)
    else:
        b = np.append(b, check_adj(a, i))

#%%
# ANSWER 2
print(np.prod(b[np.argsort(b)][-3:]))
