import re
from collections import Counter

f = open("2016/input_04.txt", "r")
instructions = f.readlines()
instructions = [i[:-1] for i in instructions]
real_rooms = []

final_sum = 0
for s in instructions:
    r = re.search(r"(.+)-(\d{3})\[(.{5})\]", s)

    name = r.groups()[0].replace("-", "")

    sector_id = int(r.groups()[1])

    checksum = r.groups()[2]

    c = Counter(sorted(list(name)))
    result = ""
    for k, v in c.most_common()[:5]:
        result += k

    if result == checksum:
        final_sum += sector_id
        real_rooms.append(s)

# ANSWER 1
print(final_sum)

for room in real_rooms:
    r = re.search(r"(.+)-(\d{3})\[(.{5})\]", room)

    name = r.groups()[0].replace("-", " ")

    sector_id = int(r.groups()[1])

    decrypted = ""
    for i in name:
        if i == " ":
            decrypted += " "
            continue
        x = ord(i) + (sector_id % 26)
        if x > ord("z"):
            x = x - ord("z") + ord("a") - 1
        decrypted += chr(x)

    if decrypted == "northpole object storage":
        # ANSWER 2
        print(sector_id)
        break
