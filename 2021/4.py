# %%
import numpy as np
import pandas as pd

f = open('2021/input_4.txt', 'r')
lines = f.readlines()

# %%
draws = lines[0]
lines = lines[1:]

# %%
for i in range(0, len(lines)):
    lines[i] = lines[i].replace('\n', '')

# %%
bingos = []
for i in range(0, int(len(lines)/6)):
    x = lines[(1+6*i):(6+6*i)]
    x = [t.split(' ') for t in x]
    for y in range(0, len(x)):
        x[y] = [int(n) for n in x[y] if n != '']
    bingos.append(x)

for i in range(0, len(bingos)):
    bingos[i] = np.array(bingos[i])
    bingos[i] = pd.DataFrame(bingos[i])
 
# %%
draws = draws[:-1].split(',')
draws = [int(d) for d in draws]

# %%
bindex = bingos.copy()
minvalue = 500
minindex = -1
for i in range(0, len(bindex)):
    bindex[i] = bindex[i].applymap(lambda x: draws.index(x))
    m = min(min(bindex[i].max(axis=0)), min(bindex[i].max(axis=1)))
    if m < minvalue:
        minvalue = m
        minindex = i

# %%
finals = draws[:minvalue+1]
df = bingos[minindex]
unmarkd = df.applymap(lambda x: 0 if x in finals else x).to_numpy().sum()

# ANSWER 1
print(unmarkd * draws[minvalue])

# %%
bindex = bingos.copy()
maxvalue = -1
maxindex = -1
for i in range(0, len(bindex)):
    bindex[i] = bindex[i].applymap(lambda x: draws.index(x))
    m = min(min(bindex[i].max(axis=0)), min(bindex[i].max(axis=1)))
    if m > maxvalue:
        maxvalue = m
        maxindex = i
# %%
finals2 = draws[:maxvalue+1]
df2 = bingos[maxindex]
unmarkd2 = df2.applymap(lambda x: 0 if x in finals2 else x).to_numpy().sum()

# ANSWER 2
print(unmarkd2 * draws[maxvalue])
