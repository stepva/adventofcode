with open("2022/input_09.txt", "r") as f:
    instructions = [i[:-1] for i in f.readlines()]

H = [50, 50]
T = [50, 50]
visited = [[0 for x in range(1000)] for x in range(1000)]
visited[T[1]][T[0]] = 1

def is_adjacent(T, H):
    Tx, Ty = T
    Hx, Hy = H
    if abs(Hx - Tx) > 1 or abs(Hy - Ty) > 1:
        return False
    return True

def move_tail(T, H):
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
    visited[T[1]][T[0]] = 1
    return T

for i in instructions:
    d, steps = i.split(' ')
    match d:
        case 'R':
            for i in range(int(steps)):
                H[0] += 1
                if not is_adjacent(T, H):
                    T = move_tail(T, H)
        case 'U':
            for i in range(int(steps)):
                H[1] += 1
                if not is_adjacent(T, H):
                    T = move_tail(T, H)
        case 'L':
            for i in range(int(steps)):
                H[0] -= 1
                if not is_adjacent(T, H):
                    T = move_tail(T, H)
        case 'D':
            for i in range(int(steps)):
                H[1] -= 1
                if not is_adjacent(T, H):
                    T = move_tail(T, H)

# ANSWER 1
print(sum([sum(x) for x in visited]))