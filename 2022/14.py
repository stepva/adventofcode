with open("2022/input_14.txt", "r") as f:
    instructions = [i[:-1] for i in f.readlines()]

ROWS = 1000
COLS = 1000
cave = [[0 for _ in range(COLS)] for _ in range(ROWS)]

for i in instructions:
    points = i.split(" -> ")
    points = [[int(x) for x in p.split(",")] for p in points]

    for p in range(len(points) - 1):
        col, row = points[p]
        next_col, next_row = points[p + 1]
        for r in range(min(row, next_row), max(row, next_row) + 1):
            for c in range(min(col, next_col), max(col, next_col) + 1):
                cave[r][c] = 1

start = (500, 0)
counter = 0
while True:
    col, row = start
    while True:
        while cave[row + 1][col] == 0 and row < ROWS - 2:
            row += 1
        if cave[row + 1][col - 1] == 0 and row < ROWS - 2 and col > 0:
            row += 1
            col -= 1
        elif cave[row + 1][col + 1] == 0 and row < ROWS - 2 and col < COLS:
            row += 1
            col += 1
        else:
            break
    if row == ROWS - 2:
        break
    cave[row][col] = 2
    counter += 1

# ANSWER 1
print(counter)

cave = [[0 for _ in range(COLS)] for _ in range(ROWS)]
max_row = 0

for i in instructions:
    points = i.split(" -> ")
    points = [[int(x) for x in p.split(",")] for p in points]

    for p in range(len(points) - 1):
        col, row = points[p]
        next_col, next_row = points[p + 1]
        for r in range(min(row, next_row), max(row, next_row) + 1):
            for c in range(min(col, next_col), max(col, next_col) + 1):
                cave[r][c] = 1
        max_row = max(max_row, max(row, next_row))
new_rows = max_row + 2
cave = cave[: new_rows + 1]

for r in range(1, new_rows):
    for c in range(1, COLS):
        if cave[r - 1][c - 1] == 1 and cave[r - 1][c] == 1 and cave[r - 1][c + 1] == 1:
            cave[r][c] = 1

rocks = sum([sum(x) for x in cave])

sand = 0
for i in range(1, new_rows + 1):
    sand += (i * 2) - 1

# ANSWER 2
print(sand - rocks)
