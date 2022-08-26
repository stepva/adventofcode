f = open("2015/input_8.txt", "r")
list_input = f.readlines()

literals = 0
memory = 0

for l in list_input:
    l = l[:-1]
    length = len(l)
    literals += length

    mem = length - 2

    l = l[1:-1]

    i = 0
    while i < len(l) - 1:
        if l[i] == "\\":
            if l[i + 1] == "x":
                mem -= 3
            elif (l[i + 1] == "\\") or (l[i + 1] == '"'):
                mem -= 1
            i += 2
        else:
            i += 1

    memory += mem

# ANSWER 1
print(literals - memory)

new_memory = 0

for l in list_input:
    l = l[1:-2]
    new_memory += 6 + len(l) + l.count("\\") + l.count('"')

# ANSWER 2
print(new_memory - literals)
