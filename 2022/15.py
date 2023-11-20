import re

with open("2022/input_15.txt", "r") as f:
    instructions = [i[:-1] for i in f.readlines()]

Y = 2000000

sensors_beacons = []
for line in instructions:
    sx, sy, bx, by = re.search(r"Sensor at x=(-?\d+), y=(-?\d+): closest beacon is at x=(-?\d+), y=(-?\d+)", line).groups()
    sx, sy, bx, by = int(sx), int(sy), int(bx), int(by)
    d = abs(sx - bx) + abs(sy - by)
    sensors_beacons.append((sx, sy, bx, by, d))

beacons_Y = []
borders = []

for s_b in sensors_beacons:
    sx, sy, bx, by, d = s_b
    dist_s_b_y = abs(sy - Y)

    if dist_s_b_y > d:
        continue

    bx_side = abs(d - dist_s_b_y)
    bx_len = 2 * bx_side + 1
    
    border = [sx - bx_side, sx + bx_side]
    borders.append(border)

    if by == Y:
        beacons_Y.append(bx)

borders = sorted(borders, key=lambda x: x[0])
new_borders = [borders[0]]

for b in borders[1:]:
    if b[0] <= new_borders[-1][1]:
        if b[1] > new_borders[-1][1]:
            new_borders[-1][1] = b[1]
    else:
        new_borders.append(b)

beacons_Y = list(set(beacons_Y))

x = 0
for b in new_borders:
    x += b[1] - b[0] + 1
    for i in range(len(beacons_Y)):
        if beacons_Y[i] >= b[0] and beacons_Y[i] <= b[1]:
            x -= 1
            beacons_Y.pop(i)

# ANSWER 1            
print(x)


# yeah, I know that this is a very ineffective and long loop, but.. it's 11/2023 and I just got back to this
max_xy = 4000000

X = 0
for Y in range(0, max_xy):
    borders = []

    for s_b in sensors_beacons:
        sx, sy, bx, by, d = s_b
        dist_s_b_y = abs(sy - Y)

        if dist_s_b_y > d:
            continue

        bx_side = abs(d - dist_s_b_y)
        bx_len = 2 * bx_side + 1
        
        border = [sx - bx_side, sx + bx_side]
        border = [max(0, border[0]), min(max_xy, border[1])]
        borders.append(border)

    borders = sorted(borders, key=lambda x: x[0])
    new_borders = [borders[0]]

    for b in borders[1:]:
        if b[0] <= new_borders[-1][1]:
            if b[1] > new_borders[-1][1]:
                new_borders[-1][1] = b[1]
        else:
            new_borders.append(b)

    x = 0
    for b in new_borders:
        x += b[1] - b[0] + 1

    if x != max_xy + 1:
        for i in range(len(new_borders)):
            if i == 0:
                if new_borders[i][0] > 0:
                    break
            else:
                if new_borders[i][0] > new_borders[i-1][1]:
                    X = new_borders[i][0] - 1
                    break
        break

# ANSWER 2
print(X * 4000000 + Y)


