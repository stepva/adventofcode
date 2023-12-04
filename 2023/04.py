with open("2023/input_04.txt", "r") as f:
    instructions = [i[:-1] for i in f.readlines()]

def part_one(instructions):
    points = 0

    for i in instructions:
        winning, have = i.split(': ')[1].split(' | ')
        winning = set([int(x) for x in winning.split(' ') if x != ''])
        have = set([int(x) for x in have.split(' ') if x != ''])
        n_same = len(winning.intersection(have))
        if n_same > 0:
            worth = 1*(2**(n_same-1))
            points += worth
    
    return points

# ANSWER 1
print(part_one(instructions))


def part_two(instructions):
    copies_won = {}

    for card, i in enumerate(instructions):
        card+=1
        winning, have = i.split(': ')[1].split(' | ')
        winning = set([int(x) for x in winning.split(' ') if x != ''])
        have = set([int(x) for x in have.split(' ') if x != ''])
        n_same = len(winning.intersection(have))
        copies = copies_won.get(card, 1)
        
        for j in range(n_same):
            copies_won[card+j+1] = copies_won.get(card+j+1, 1) + copies
        
        copies_won[card] = copies
    
    return sum(copies_won.values())

# ANSWER 2
print(part_two(instructions))

