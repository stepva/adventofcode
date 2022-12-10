with open("2022/input_09.txt", "r") as f:
    instructions = [i[:-1] for i in f.readlines()]

# function to check if is adjacent
def is_adjacent(T, H):
    if abs(H[0] - T[0]) > 1 or abs(H[1] - T[1]) > 1:
        return False
    return True

# function to move tail to head (or knot to previous one in part 2) 
# and count it if it's the last knot
def move_tail(T, H, add_to, count=True):
    Tx, Ty = T
    Hx, Hy = H
    if Hx > Tx:
        if Hy == Ty:
            T = [Tx + 1, Ty]
        elif Hy > Ty:
            T = [Tx+1, Ty+1]
        elif Hy < Ty:
            T = [Tx+1, Ty-1]
    elif Hx < Tx:
        if Hy == Ty:
            T = [Tx-1, Ty]
        elif Hy > Ty:
            T = [Tx-1, Ty+1]
        elif Hy < Ty:
            T = [Tx-1, Ty-1]
    elif Hx == Tx:
        if Hy > Ty:
            T = [Tx, Ty+1]
        elif Hy < Ty:
            T = [Tx, Ty-1]
    if count:
        add_to[T[1]][T[0]] = 1
    return T

# initialize, part 1
H = [500, 500]
T = [500, 500]
visited = [[0 for x in range(1000)] for x in range(1000)]
visited[T[1]][T[0]] = 1

# main loop, part 1
for i in instructions:
    d, steps = i.split(' ')
    match d:
        case 'R':
            for i in range(int(steps)):
                H[0] += 1
                if not is_adjacent(T, H):
                    T = move_tail(T, H, add_to=visited)
        case 'U':
            for i in range(int(steps)):
                H[1] += 1
                if not is_adjacent(T, H):
                    T = move_tail(T, H, add_to=visited)
        case 'L':
            for i in range(int(steps)):
                H[0] -= 1
                if not is_adjacent(T, H):
                    T = move_tail(T, H, add_to=visited)
        case 'D':
            for i in range(int(steps)):
                H[1] -= 1
                if not is_adjacent(T, H):
                    T = move_tail(T, H, add_to=visited)

# ANSWER 1
print(sum([sum(x) for x in visited]))

# initialize, part 2
rope = [[500, 500] for x in range(10)]
visited_2 = [[0 for x in range(1000)] for x in range(1000)]
visited_2[rope[-1][1]][rope[-1][0]] = 1

# function to move the whole rope, part 2
def move_rope():
    for i in range(1, 10):
        count = True if i == 9 else False
        if not is_adjacent(rope[i], rope[i-1]):
            rope[i] = move_tail(rope[i], rope[i-1], add_to=visited_2, count=count)

# main loop, part 2
for i in instructions:
    d, steps = i.split(' ')
    match d:
        case 'R':
            for i in range(int(steps)):
                rope[0][0] += 1
                move_rope()
        case 'U':
            for i in range(int(steps)):
                rope[0][1] += 1
                move_rope()
        case 'L':
            for i in range(int(steps)):
                rope[0][0] -= 1
                move_rope()
        case 'D':
            for i in range(int(steps)):
                rope[0][1] -= 1
                move_rope()

# ANSWER 2
print(sum([sum(x) for x in visited_2]))