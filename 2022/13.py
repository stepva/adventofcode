with open("2022/input_13.txt", "r") as f:
    instructions = [i[:-1] for i in f.readlines()]

indices = []


def compare(left, right):
    global in_order
    if in_order:
        return True

    if isinstance(left, int) and isinstance(right, list):
        left = [left]

    if isinstance(left, list) and isinstance(right, int):
        right = [right]

    if isinstance(left, int) and isinstance(right, int):
        if left > right:
            return True
        elif left < right:
            in_order = True
            return True

    elif isinstance(left, list) and isinstance(right, list):
        for j in range(max(len(left), len(right))):
            if j >= len(left):
                in_order = True
                return True
            elif j >= len(right):
                return True
            if compare(left[j], right[j]):
                return True

    return False


n = 0
for i in range(0, len(instructions), 3):
    n += 1
    left = eval(instructions[i])
    right = eval(instructions[i + 1])

    in_order = False
    compare(left, right)
    if in_order:
        indices.append((i // 3) + 1)

# ANSWER 1
print(sum(indices))

decoder_1 = [[2]]
decoder_2 = [[6]]

packets = [eval(i) for i in instructions if i] + [decoder_1] + [decoder_2]

# insertion sort
i = 1
while i < len(packets):
    j = i
    in_order = False
    compare(packets[j - 1], packets[j])
    while j > 0 and not in_order:
        packets = packets[: j - 1] + [packets[j], packets[j - 1]] + packets[j + 1 :]
        j -= 1
        in_order = False
        compare(packets[j - 1], packets[j])
    in_order = False
    i += 1

# ANSWER 2
print((packets.index(decoder_1) + 1) * (packets.index(decoder_2) + 1))
