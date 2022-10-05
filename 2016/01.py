#%%
f = open("2016/input_01.txt", "r")
instructions = f.readlines()[0][:-1]
instructions = instructions.split(', ')

# %%
left = 0
right = 0
up = 0
down = 0

if instructions[0][0] == "L":
    left += int(instructions[0][1:])
else:
    right += int(instructions[0][1:])

#%%
for i in range(1, len(instructions)):
    match instructions[i][0]:
        case "L":
            match instructions[i-1][0]:
                case "U":
                    left += int(instructions[i][1:])
                case "L":
                    instructions[i] = "D" + instructions[i][1:]
                    down += int(instructions[i][1:])
                case "D":
                    instructions[i] = "R" + instructions[i][1:]
                    right += int(instructions[i][1:])
                case "R":
                    instructions[i] = "U" + instructions[i][1:]
                    up += int(instructions[i][1:])
        case "R":
            match instructions[i-1][0]:
                case "U":
                    right += int(instructions[i][1:])
                case "L":
                    instructions[i] = "U" + instructions[i][1:]
                    up += int(instructions[i][1:])
                case "D":
                    instructions[i] = "L" + instructions[i][1:]
                    left += int(instructions[i][1:])
                case "R":
                    instructions[i] = "D" + instructions[i][1:]
                    down += int(instructions[i][1:])

# %%
x = abs(left - right)
y = abs(up - down)

# ANSWER 1
print(x + y)

# %%
l = (max(left, right, up, down)+1) * 2
m = [[0 for i in range(l)] for i in range(l)]

start = int(l / 2)
m[start][start] = 1
last_x = start
last_y = start

for i in instructions:
    match i[0]:
        case "U":
            for i in range(1, int(i[1:]) + 1):
                m[last_y - 1][last_x] += 1
                last_y -= 1
                if m[last_y][last_x] > 1:
                    break
        case "L":
            for i in range(1, int(i[1:]) + 1):
                m[last_y][last_x - 1] += 1
                last_x -= 1
                if m[last_y][last_x] > 1:
                    break
        case "D":
            for i in range(1, int(i[1:]) + 1):
                m[last_y + 1][last_x] += 1
                last_y += 1
                if m[last_y][last_x] > 1:
                    break
        case "R":
            for i in range(1, int(i[1:]) + 1):
                m[last_y][last_x + 1] += 1
                last_x += 1
                if m[last_y][last_x] > 1:
                    break
    
    if any(any(j for j in row if j > 1) for row in m):
        break

# ANSWER 2
print(abs((abs(last_x) - start)) + abs((abs(last_y) - start)))