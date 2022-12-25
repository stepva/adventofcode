with open("2022/input_12.txt", "r") as f:
    instructions = [i[:-1] for i in f.readlines()]

heightmap = []

for r in range(len(instructions)):
    row = []
    for c in range(len(instructions[r])):
        if instructions[r][c] == "S":
            S = (r, c)
            row.append(0)
        elif instructions[r][c] == "E":
            E = (r, c)
            row.append(25)
        else:
            row.append(ord(instructions[r][c]) - ord("a"))
    heightmap.append(row)


def find_path():
    options = [(S, 0)]
    checked = set()

    while options:
        current, n = options.pop(0)

        if current == E:
            return n

        for d in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            new_r = current[0] + d[0]
            new_c = current[1] + d[1]

            if (
                new_r < 0
                or new_r >= len(heightmap)
                or new_c < 0
                or new_c >= len(heightmap[current[0]])
                or (new_r, new_c) in checked
            ):
                continue
            elif heightmap[new_r][new_c] - heightmap[current[0]][current[1]] <= 1:
                options.append(((new_r, new_c), n + 1))
                checked.add((new_r, new_c))


# ANSWER 1
print(find_path())


def find_path2():
    options = [(E, 0)]
    checked = set()

    while options:
        current, n = options.pop(0)

        if heightmap[current[0]][current[1]] == 0:
            return n

        for d in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            new_r = current[0] + d[0]
            new_c = current[1] + d[1]

            if (
                new_r < 0
                or new_r >= len(heightmap)
                or new_c < 0
                or new_c >= len(heightmap[current[0]])
                or (new_r, new_c) in checked
            ):
                continue
            elif heightmap[current[0]][current[1]] - heightmap[new_r][new_c] <= 1:
                options.append(((new_r, new_c), n + 1))
                checked.add((new_r, new_c))


# ANSWER 2
print(find_path2())
