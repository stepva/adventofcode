f = open("2020/input_02.txt", "r")
lines = f.readlines()

valid_1 = 0
valid_2 = 0

for l in lines:
    s = l.split(" ")

    borders = s[0].split("-")
    borders = [int(b) for b in borders]

    letter = s[1][0]

    n = len([c for c in s[2] if c == letter])
    if n >= borders[0] and n <= borders[1]:
        valid_1 += 1

    both = s[2][borders[0] - 1] == letter and s[2][borders[1] - 1] == letter
    some = s[2][borders[0] - 1] == letter or s[2][borders[1] - 1] == letter
    if some and not both:
        valid_2 += 1

# ANSWER 1
print(valid_1)

# ANSWER 2
print(valid_2)
