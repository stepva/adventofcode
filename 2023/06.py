from timeit import default_timer as timer

with open("2023/input_06.txt", "r") as f:
    instructions = [i[:-1] for i in f.readlines()]


def get_distance(press, time):
    return (time-press) * press


def part_one(instructions):
    for i in instructions:
        if i.startswith('Time:'):
            times = [int(x) for x in i.split(' ')[1:] if x != '']
        elif i.startswith('Distance'):
            distances = [int(x) for x in i.split(' ')[1:] if x != '']

    races = list(zip(times, distances))
    margins = 1

    for time, record in races:
        options = 0
        for press in range(1, time):
            if get_distance(press, time) > record:
                options += 1
        margins = margins * max(options, 1)
    
    return margins

# ANSWER 1
print(part_one(instructions))

def part_two(instructions):
    for i in instructions:
        if i.startswith('Time:'):
            time = int(''.join([x for x in i.split(' ')[1:] if x != '']))
        elif i.startswith('Distance'):
            record = int(''.join([x for x in i.split(' ')[1:] if x != '']))  

    options = 0
    for press in range(1, time):
        if get_distance(press, time) > record:
            options += 1
    
    return options

# ANSWER 2 (bruteforce hehe)
print(part_two(instructions))

def part_two_faster(instructions):
    for i in instructions:
        if i.startswith('Time:'):
            time = int(''.join([x for x in i.split(' ')[1:] if x != '']))
        elif i.startswith('Distance'):
            record = int(''.join([x for x in i.split(' ')[1:] if x != '']))  

    for press in range(1, time):
        if get_distance(press, time) > record:
            lower_option = press
            break

    for press in range(time, lower_option, -1):
        if get_distance(press, time) > record:
            upper_option = press
            break

    return upper_option - lower_option + 1

# ANSWER 2 (faster, almost 4x)
print(part_two_faster(instructions))




