with open("2023/input_03.txt", "r") as f:
    instructions = [i[:-1] for i in f.readlines()]

def is_symbol(c):
    if c == '.' or c.isdigit():
        return False
    return True

def symbol_around(x, y, grid):
    max_x = len(grid[y]) - 1
    max_y = len(grid) - 1

    for X in range(max(x-1, 0), min(x+1, max_x)+1):
        for Y in range(max(y-1, 0), min(y+1, max_y)+1):
            if is_symbol(grid[Y][X]):
                return True

def part_one(instructions):
    parts_sum = 0

    for y, line in enumerate(instructions):
        current_number = ''
        adjacent_symbol = False
        for x, c in enumerate(line+'.'):
            if not c.isdigit() or x == len(line):
                if len(current_number) > 0 and adjacent_symbol:
                    parts_sum += int(current_number)
                    
                current_number = ''
                adjacent_symbol = False
                continue
            
            current_number += c
            if symbol_around(x, y, instructions):
                adjacent_symbol = True
    
    return parts_sum

# ANSWER 1
print(part_one(instructions))

            
def get_full_number(x, line):
    for X_1 in range(x, -2, -1):
        if not (line[X_1]).isdigit():
            X_1 += 1
            break
    for X_2 in range(x, len(line)):
        if not (line[X_2]).isdigit():
            X_2 -= 1
            break
    
    return int(line[X_1:X_2+1])
            
def numbers_around(x, y, grid):
    max_x = len(grid[y]) - 1
    max_y = len(grid) - 1

    numbers_checked = []
    numbers = []

    for X in range(max(x-1, 0), min(x+1, max_x)+1):
        for Y in range(max(y-1, 0), min(y+1, max_y)+1):
            if (grid[Y][X]).isdigit():
                if (X-1, Y) not in numbers_checked:
                    numbers.append(get_full_number(X, grid[Y]))
                numbers_checked.append((X, Y))
    
    return numbers

def part_two(instructions):
    gears_sum = 0

    for y, line in enumerate(instructions):
        for x, c in enumerate(line):
            if c == '*':
                numbers = numbers_around(x, y, instructions)
                if len(numbers) == 2:
                    gears_sum += numbers[0] * numbers[1]

    return gears_sum

# ANSWER 2
print(part_two(instructions))