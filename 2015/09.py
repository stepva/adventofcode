from itertools import permutations

with open("2015/input_09.txt", "r") as f:
    instructions = [i[:-1] for i in f.readlines()]

graph = {}
for i in instructions:
    path, n = i.split(" = ")
    a, b = path.split(" to ")
    if a not in graph:
        graph[a] = {}
    graph[a][b] = int(n)
    if b not in graph:
        graph[b] = {}
    graph[b][a] = int(n)

places = graph.keys()
min_path = None
min_dist = 0

for p in places:
    current = p
    visited = [current]
    distance = 0

    while len(visited) < len(places):
        for city, dist in sorted(graph[current].items(), key=lambda x: x[1]):
            if city not in visited:
                visited.append(city)
                distance += dist
                current = city
                break

    if distance < min_dist or min_dist == 0:
        min_dist = distance
        min_path = visited


# print(min_path)
# ANSWER 1
print(min_dist)

max_path = None
max_dist = 0

for way in permutations(places):
    distance = 0
    for i in range(1, len(way)):
        distance += graph[way[i - 1]][way[i]]

    if distance > max_dist:
        max_dist = distance
        max_path = list(way)

# print(max_path)
# ANSWER 2
print(max_dist)

# meh I don't really like the solution to part 2, using permutations and going through every possible one
# I sort of gave up there and went to reddit for help :(
# I feel like there has to be some nicer (ie. cleverer, not brute-force) solution, like to part 1, but idk
