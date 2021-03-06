# %%
f = open('2021/input_2.txt', 'r')

#%%
hor, dep = 0, 0
for i in f.readlines():
    c = i.split(" ")
    steps = int(c[1])
    match c[0]:
        case 'forward':
            hor += steps
        case 'down':
            dep += steps
        case 'up':
            dep -= steps

# ANSWER 1        
print(hor * dep)

# %%
f = open('2021/input_2.txt', 'r')

# %%
hor, dep, aim = 0, 0, 0
for i in f.readlines():
    c = i.split(" ")
    steps = int(c[1])
    match c[0]:
        case 'forward':
            hor += steps
            dep += aim * steps
        case 'down':
            aim += steps
        case 'up':
            aim -= steps

# ANSWER 2
print(hor * dep)

# %%
