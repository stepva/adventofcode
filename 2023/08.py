from math import lcm

with open("2023/input_08.txt", "r") as f:
    instructions = [i[:-1] for i in f.readlines()]

nodes = {}

for i in instructions[2:]:
    main, lr = i.split(' = ')
    left, right = lr.rstrip(')').lstrip('(').split(', ')
    nodes[main] = {'L': left, 'R': right}

instructions = instructions[0]

def part_one(nodes, instructions):
    n_inst = len(instructions)
    i = 0
    node = 'AAA'
    lr = instructions[i % n_inst]

    while nodes[node][lr] != 'ZZZ':
        i += 1
        node = nodes[node][lr]
        lr = instructions[i % n_inst]

    return i + 1

# ANSWER 1
print(part_one(nodes, instructions))


def part_two(nodes, instructions):
    n_inst = len(instructions)

    starting_nodes = [n for n in nodes.keys() if n.endswith('A')]
    steps = []

    for s_node in starting_nodes:
        i = 0
        node = s_node
        lr = instructions[i % n_inst]

        while not nodes[node][lr].endswith('Z'):
            i += 1
            node = nodes[node][lr]
            lr = instructions[i % n_inst]
        
        steps.append(i+1)
        
    return lcm(*steps)
    

# ANSWER 2
print(part_two(nodes, instructions))