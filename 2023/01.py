import re

with open("2023/input_01.txt", "r") as f:
    instructions = [i[:-1] for i in f.readlines()]

calibration_value = 0
for i in instructions:
    digits = [c for c in i if c.isdigit()]
    value = int(''.join([digits[0], digits[-1]]))
    calibration_value += value

# ANSWER 1
print(calibration_value)

calibration_value = 0
wordigits = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
reg = re.compile(r'(?=(\d|one|two|three|four|five|six|seven|eight|nine))')

for i in instructions:
    digits = re.findall(reg, i)
    digits = [digits[0], digits[-1]]
    digits = [str(wordigits.index(d)+1) if not d.isdigit() else d for d in digits ]
    value = int(''.join([digits[0], digits[-1]]))
    calibration_value += value

# ANSWER 2
print(calibration_value)


    



