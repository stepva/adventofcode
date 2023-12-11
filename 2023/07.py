from collections import Counter

with open("2023/input_07.txt", "r") as f:
    instructions = [i[:-1] for i in f.readlines()]

hands = {i.split(' ')[0]: int(i.split(' ')[1]) for i in instructions}

def get_hand_strength(hand):
    strengths = [[1, 1, 1, 1, 1],
             [1, 1, 1, 2],
             [1, 2, 2],
             [1, 1, 3],
             [2, 3],
             [1, 4],
             [5]]
    
    return strengths.index(sorted(Counter(hand).values()))

def compare_hands(left, right):
    cards = ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2']
    left_strenght = get_hand_strength(left)
    right_strenght = get_hand_strength(right)

    if left_strenght < right_strenght:
        return left, right
    elif left_strenght > right_strenght:
        return right, left
    else:
        for i in range(len(left)):
            left_card_strength = cards.index(left[i])
            right_card_strength = cards.index(right[i])
            if left_card_strength < right_card_strength:
                return right, left
            elif left_card_strength > right_card_strength:
                return left, right


def part_one(hands):
    ordered_hands = [list(hands.keys())[0]]

    for hand in list(hands.keys())[1:]:
        for i in range(len(ordered_hands)):
            left, _ = compare_hands(ordered_hands[i], hand)
            if left == hand:
                ordered_hands = ordered_hands[:i] + [hand] + ordered_hands[i:]
                break
            if i == len(ordered_hands)-1:
                ordered_hands.append(hand)

    winnings = 0

    for i in range(len(ordered_hands)):
        winnings += hands[ordered_hands[i]] * (i+1)

    return winnings

# ANSWER 1
print(part_one(hands))


def get_J_strength(hand):
    strength = get_hand_strength(hand)
    js = Counter(hand)['J']
    
    if js == 0:
        return strength

    if strength == 5 and js > 0:
        strength = 6
    elif strength == 4 and js > 0:
        strength = 6
    elif strength == 3 and js > 0:
        strength = 5
    elif strength == 2 and js > 0:
        if js == 1:
            strength = 4
        elif js == 2:
            strength = 5
    elif strength == 1 and js > 0:
        strength = 3
    elif strength == 0 and js > 0:
        strength = 1
    
    return strength


def compare_hands_two(left, right):
    cards = ['A', 'K', 'Q', 'T', '9', '8', '7', '6', '5', '4', '3', '2', 'J']

    left_strenght = get_J_strength(left)
    right_strenght = get_J_strength(right)

    if left_strenght < right_strenght:
        return left, right
    elif left_strenght > right_strenght:
        return right, left
    else:
        for i in range(len(left)):
            left_card_strength = cards.index(left[i])
            right_card_strength = cards.index(right[i])
            if left_card_strength < right_card_strength:
                return right, left
            elif left_card_strength > right_card_strength:
                return left, right


def part_two(hands):
    ordered_hands = [list(hands.keys())[0]]

    for hand in list(hands.keys())[1:]:
        for i in range(len(ordered_hands)):
            left, _ = compare_hands_two(ordered_hands[i], hand)
            if left == hand:
                ordered_hands = ordered_hands[:i] + [hand] + ordered_hands[i:]
                break
            if i == len(ordered_hands)-1:
                ordered_hands.append(hand)

    winnings = 0

    for i in range(len(ordered_hands)):
        winnings += hands[ordered_hands[i]] * (i+1)

    return winnings
    
# ANSWER 2
print(part_two(hands))