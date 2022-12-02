f = open("2022/input_02.txt", "r")
instructions = [i[:-1] for i in f.readlines()]

scores = {"X": 1, "Y": 2, "Z": 3}
wins = {"X": "C", "Y": "A", "Z": "B"}
draws = {"X": "A", "Y": "B", "Z": "C"}

total_score = 0

for i in instructions:
    elf, me = i.split(" ")
    total_score += scores[me]
    if elf == wins[me]:
        total_score += 6
    elif elf == draws[me]:
        total_score += 3

# ANSWER 1
print(total_score)

wins = {v: k for k, v in wins.items()}
draws = {v: k for k, v in draws.items()}
loses = {'B': 'X', 'C': 'Y', 'A': 'Z'}

total_score_2 = 0

for i in instructions:
    elf, need = i.split(" ")
    match need:
        case 'X':
            total_score_2 += scores[loses[elf]] + 0
        case 'Y':
            total_score_2 += scores[draws[elf]] + 3
        case 'Z':
            total_score_2 += scores[wins[elf]] + 6

# ANSWER 2
print(total_score_2)
    