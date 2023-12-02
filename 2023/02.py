with open("2023/input_02.txt", "r") as f:
    instructions = [i[:-1] for i in f.readlines()]

limits = {'red': 12, 'green': 13, 'blue': 14}
id_sum = 0

for i in instructions:
    game_id, subsets = i.split(':')
    game_id = int(game_id.split(' ')[1])
    subsets = subsets.split(';')
    all_subsets_possible = True
    for s in subsets:
        draws = s.split(',')
        for d in draws:
            n, color = d.lstrip().rstrip().split(' ')
            if int(n) > limits[color]:
                all_subsets_possible = False
                break
    if all_subsets_possible:
        id_sum += game_id

# ANSWER 1
print(id_sum)

power_sum = 0

for i in instructions:
    game_id, subsets = i.split(':')
    game_id = int(game_id.split(' ')[1])
    subsets = subsets.split(';')
    min_numbers = {'red': 0, 'green': 0, 'blue': 0}
    for j, s in enumerate(subsets):
        draws = s.split(',')
        for d in draws:
            n, color = d.lstrip().rstrip().split(' ')
            min_numbers[color] = max(min_numbers[color], int(n))
    game_power = min_numbers['red'] * min_numbers['blue'] * min_numbers['green']
    power_sum += game_power

# ANSWER 2
print(power_sum)