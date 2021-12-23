f = open("2015/input_2.txt", "r")
lines = f.readlines()

paper = 0
ribbon = 0

for i in lines:
    i = i[:-1]
    sizes = i.split("x")
    l = int(sizes[0])
    w = int(sizes[1])
    h = int(sizes[2])
    dims = [l, w, h]
    smallest = min([l * w, w * h, h * l])
    area = 2 * l * w + 2 * w * h + 2 * h * l
    paper += area + smallest

    small_1 = min(dims)
    dims.remove(small_1)
    small_2 = min(dims)
    wrap = small_1 * 2 + small_2 * 2
    bow = l * w * h
    ribbon += wrap + bow

# ANSWER 1
print(paper)
# ASNWER 2
print(ribbon)
