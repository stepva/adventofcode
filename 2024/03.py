import re

with open("2024/input_03.txt", "r") as f:
    instructions = [i[:-1] for i in f.readlines()]

instructions = "".join(instructions)    

results = re.findall(r"mul\((\d{1,3},\d{1,3})\)", instructions)

mul = 0
for r in results:
    x, y = r.split(",")
    mul += int(x) * int(y)

#ANSWER 1
print(mul)

results = re.findall(r"mul\(\d{1,3},\d{1,3}\)|don't\(\)|do\(\)", instructions)

mul = 0
multiply = True
for r in results:
    if r == "don't()":
        multiply = False
    elif r == "do()":
        multiply = True
    else:
        if multiply:
            x, y = re.findall(r"\d{1,3}", r)
            mul += int(x) * int(y)

# ANSWER 2
print(mul)