with open("2022/input_11.txt", "r") as f:
    instructions = [i[:-1] for i in f.readlines()]


class Monkey:
    def __init__(self, id, items, operation, test) -> None:
        self.id = id
        self.items = items
        self.operation = operation
        self.test = test
        self.counter = 0

    def item_turn(self, item):
        item = self.operation(item)
        self.counter += 1
        item = item // 3
        return item, self.test(item)

    def get_item(self, item):
        self.items.append(item)


# assuming only + or * operations here
def get_operation(line):
    line = line.split("=")[-1].replace(" ", "")
    if "*" in line:
        left, right = line.split("*")
        if left == "old" and right != "old":
            return lambda x: x * int(right)
        elif left == "old" and right == "old":
            return lambda x: x * x
    elif "+" in line:
        left, right = line.split("+")
        if left == "old" and right != "old":
            return lambda x: x + int(right)
        elif left == "old" and right == "old":
            return lambda x: x + x


def get_test(lines):
    d = int(lines[0].split(" ")[-1])
    t = int(lines[1].split(" ")[-1])
    f = int(lines[2].split(" ")[-1])
    return lambda x: t if x % d == 0 else f


monkeys = []

for i in range(len(instructions)):
    if instructions[i].startswith("Monkey"):
        id_ = int(instructions[i].split(" ")[-1][:-1])
        items_ = [int(x.replace(" ", "")) for x in instructions[i + 1].split(":")[-1].split(",")]
        operation_ = get_operation(instructions[i + 2])
        test_ = get_test(instructions[i + 3 : i + 6])
        monkeys.append(Monkey(id_, items_, operation_, test_))

for i in range(20):
    for M in monkeys:
        for i in M.items:
            new_item, new_monkey = M.item_turn(i)
            monkeys[new_monkey].get_item(new_item)
        M.items = []

monkey_business = sorted([M.counter for M in monkeys], reverse=True)
# ANSWER 1
print(monkey_business[0] * monkey_business[1])
