with open("2024/input_01.txt", "r") as f:
    instructions = [i[:-1] for i in f.readlines()]

left, right = [], []

for i in instructions:
    l, r = i.split("   ")
    left.append(int(l))
    right.append(int(r))

left = sorted(left)
right = sorted(right)

diff_sum = 0
for i in range(len(left)):
    diff_sum += abs(left[i] - right[i])

# ANSWER 1
print(diff_sum)

from collections import Counter

right_counter = Counter(right)

similarity_score = 0
for l in left:
    similarity_score += l * right_counter[l]

# ANSWER 2
print(similarity_score)
