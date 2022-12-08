with open("2022/input_08.txt", "r") as f:
    instructions = [i[:-1] for i in f.readlines()]

rows = [list(x) for x in instructions]
rows = [[int(x) for x in y] for y in rows]

cols = list(map(list, zip(*rows)))

counted = [[0 for c in cols] for i in rows]

for j in range(len(rows)):
    r = rows[j]
    m = max(r)
    for i in range(len(r)):
        if i == 0:
            counted[j][i] = 1
        else:
            if r[i] > max(r[:i]):
                counted[j][i] = 1
        if r[i] == m:
            break

    for i in range(len(r) - 1, 0, -1):
        if i == len(r) - 1:
            counted[j][i] = 1
        else:
            if r[i] > max(r[i + 1 :]):
                counted[j][i] = 1
        if r[i] == m:
            break

for j in range(len(cols)):
    c = cols[j]
    m = max(c)
    for i in range(len(c)):
        if i == 0:
            counted[i][j] = 1
        else:
            if c[i] > max(c[:i]):
                counted[i][j] = 1
        if c[i] == m:
            break

    for i in range(len(c) - 1, 0, -1):
        if i == len(c) - 1:
            counted[i][j] = 1
        else:
            if c[i] > max(c[i + 1 :]):
                counted[i][j] = 1
        if c[i] == m:
            break

# ANSWER 1
print(sum([sum(x) for x in counted]))

scenic = [[0 for c in cols] for i in rows]

for j in range(len(rows)):
    for i in range(len(r)):
        left = 0
        for n in range(i - 1, -1, -1):
            left += 1
            if rows[j][i] <= rows[j][n]:
                break

        right = 0
        for n in range(i + 1, len(rows[j])):
            right += 1
            if rows[j][i] <= rows[j][n]:
                break

        up = 0
        for n in range(j - 1, -1, -1):
            up += 1
            if rows[j][i] <= rows[n][i]:
                break

        down = 0
        for n in range(j + 1, len(rows)):
            down += 1
            if rows[j][i] <= rows[n][i]:
                break

        scenic[j][i] = left * right * up * down

# ANSWER 2
print(max([max(x) for x in scenic]))
