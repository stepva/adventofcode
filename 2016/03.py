#%%
import numpy as np

#%%
f = open("2016/input_03.txt", "r")
instructions = f.readlines()
instructions = [i[:-1].split(" ") for i in instructions]
instructions = [[int(x) for x in i if x != ""] for i in instructions]

# %%
count = 0
for i in instructions:
    m = max(i)
    max_i = i.index(m)
    if sum(i[:max_i] + i[max_i + 1 :]) > m:
        count += 1

# ANSWER 1
print(count)

#%%
np_ins = np.array(instructions)
new_ins = []
for i in range(3, len(np_ins) + 1, 3):
    g = np_ins[max(0, i - 3) : i]
    for j in np.transpose(g):
        new_ins.append(list(j))

# %%
count_2 = 0
for i in new_ins:
    m = max(i)
    max_i = i.index(m)
    if sum(i[:max_i] + i[max_i + 1 :]) > m:
        count_2 += 1

# ANSWER 2
print(count_2)
