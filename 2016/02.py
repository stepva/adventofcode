#%%
f = open("2016/input_02.txt", "r")
instructions = f.readlines()
instructions = [i[:-1] for i in instructions]

# %%
pad = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
code = ''

# %%
pos = [1, 1]
for i in instructions:

    for d in i:
        match d:
            case "U":
                pos[0] = max(0, pos[0] - 1)
            case "L":
                pos[1] = max(0, pos[1] - 1)
            case "D":
                pos[0] = min(2, pos[0] + 1)
            case "R":
                pos[1] = min(2, pos[1] + 1)

    code += str(pad[pos[0]][pos[1]])

# ANSWER 1
print(code)

# %%
pad = [[0, 0, 1, 0, 0], [0, 2, 3, 4, 0], [5, 6, 7, 8, 9], [0, 'A', 'B', 'C', 0], [0, 0, 'D', 0, 0]]
code = ''

# %%
pos = [2, 0]
for i in instructions:

    for d in i:
        match d:
            case "U":
                pos[0] = max(0, pos[0] - 1)
                if pad[pos[0]][pos[1]] == 0:
                    pos[0] += 1 
            case "L":
                pos[1] = max(0, pos[1] - 1)
                if pad[pos[0]][pos[1]] == 0:
                    pos[1] += 1 
            case "D":
                pos[0] = min(4, pos[0] + 1)
                if pad[pos[0]][pos[1]] == 0:
                    pos[0] -= 1 
            case "R":
                pos[1] = min(4, pos[1] + 1)
                if pad[pos[0]][pos[1]] == 0:
                    pos[1] -= 1 

    code += str(pad[pos[0]][pos[1]])

# ANSWER 2
print(code)