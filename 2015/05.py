import re

with open("2015/input_05.txt", "r") as f:
    instructions = [i[:-1] for i in f.readlines()]

vowels = "aeiou"

nice = 0
for i in instructions:
    if (
        sum([1 for v in i if v in vowels]) >= 3
        and re.search(r"(.)\1", i) is not None
        and re.search(r"(ab|cd|pq|xy)", i) is None
    ):
        nice += 1

# ANSWER 1
print(nice)

nice2 = 0
for i in instructions:
    if re.search(r"(.{2}).*\1", i) is not None and re.search(r"(.).\1", i) is not None:
        nice2 += 1

print(nice2)
