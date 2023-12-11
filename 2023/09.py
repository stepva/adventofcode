with open("2023/input_09.txt", "r") as f:
    instructions = [i[:-1] for i in f.readlines()]

sequences = [[int(x) for x in i.split(' ')] for i in instructions]

def part_one(sequences):
    predictions = []
    for seq in sequences:
        diffs = []
        for i in range(len(seq)-1):
            diffs.append(seq[i+1] - seq[i])
        
        last_diffs = [diffs[-1]]

        while not all([d == 0 for d in diffs]):
            new_diffs = []
            for i in range(len(diffs)-1):
                new_diffs.append(diffs[i+1] - diffs[i])
            diffs = new_diffs
            last_diffs.append(diffs[-1])

        predictions.append(seq[-1] + sum(last_diffs))
            
    return sum(predictions)

# ANSWER 1
print(part_one(sequences))

def part_two(sequences):
    predictions = []
    for seq in sequences:
        diffs = []
        for i in range(len(seq)-1):
            diffs.append(seq[i+1] - seq[i])
        first_diffs = [diffs[0]]

        while not all([d == 0 for d in diffs]):
            new_diffs = []
            for i in range(len(diffs)-1):
                new_diffs.append(diffs[i+1] - diffs[i])
            diffs = new_diffs
            first_diffs.append(diffs[0])

        main_diff = 0
        for fd in range(len(first_diffs)-2, -1, -1):
            main_diff = first_diffs[fd] - main_diff
            
        predictions.append(seq[0] - main_diff)
            
    return sum(predictions)

# ANSWER 2
print(part_two(sequences))