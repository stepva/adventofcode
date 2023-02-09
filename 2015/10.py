start = "1113222113"
new = ""

for _ in range(40):
    new = ""
    i = 0
    while True:
        n = i
        for j in range(i, len(start)):
            if start[j] == start[i]:
                n = j
            else:
                break

        new += str(len(start[i : n + 1])) + str(start[i])

        i = n + 1
        if n + 1 >= len(start):
            break
    start = new

# ANSWER 1
print(len(new))

for _ in range(10):
    new = ""
    i = 0
    while True:
        n = i
        for j in range(i, len(start)):
            if start[j] == start[i]:
                n = j
            else:
                break

        new += str(len(start[i : n + 1])) + str(start[i])

        i = n + 1
        if n + 1 >= len(start):
            break
    start = new

# ANSWER 2
print(len(new))

# brute-force eheh
# I wanted to do it with regex but couldn't figure it out
# this is a cool solution from reddit which I hoped to arrive to (it's about 2x+ faster)

# import re
# re_d = re.compile(r"((\d)\2*)")
# def replace(match_obj):
#     s = match_obj.group(1)
#     return str(len(s)) + s[0]
# s = "1113222113"
# for i in range(0):
#     s = re_d.sub(replace, s)
# print(len(s))
