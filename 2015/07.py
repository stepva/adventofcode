with open("2015/input_07.txt", "r") as f:
    instructions = [i[:-1] for i in f.readlines()]

wires = {}
n = len(instructions)
i = -1

while True:
    i += 1
    instruction = instructions[i]
    inst, wire = instruction.split(" -> ")
    if len(inst.split(" ")) == 1:
        try:
            wires[wire] = int(inst)
        except:
            if inst not in wires:
                instructions.append(instruction)
                n += 1
                continue
            wires[wire] = wires[inst]
    else:
        if "AND" in inst:
            a, b = inst.split(" AND ")
            if a == "1":
                if b not in wires:
                    instructions.append(instruction)
                    n += 1
                    continue
                wires[wire] = 1 & wires[b]
            elif a not in wires or b not in wires:
                instructions.append(instruction)
                n += 1
                continue
            else:
                wires[wire] = wires[a] & wires[b]
        elif "OR" in inst:
            a, b = inst.split(" OR ")
            if a not in wires or b not in wires:
                instructions.append(instruction)
                n += 1
                continue
            wires[wire] = wires[a] | wires[b]
        elif "LSHIFT" in inst:
            a, k = inst.split(" LSHIFT ")
            if a not in wires:
                instructions.append(instruction)
                n += 1
                continue
            wires[wire] = wires[a] << int(k)
        elif "RSHIFT" in inst:
            a, k = inst.split(" RSHIFT ")
            if a not in wires:
                instructions.append(instruction)
                n += 1
                continue
            wires[wire] = wires[a] >> int(k)
        elif "NOT" in inst:
            _, a = inst.split(" ")
            if a not in wires:
                instructions.append(instruction)
                n += 1
                continue
            wires[wire] = 65536 + ~wires[a]
    if n - i == 1 or "a" in wires:
        break

# ANSWER 1
print(wires["a"])

previous_a = wires["a"]
wires = {}
n = len(instructions)
i = -1

while True:
    i += 1
    instruction = instructions[i]
    inst, wire = instruction.split(" -> ")
    if len(inst.split(" ")) == 1:
        try:
            wires[wire] = int(inst)
            if wire == "b":
                wires[wire] = previous_a
        except:
            if inst not in wires:
                instructions.append(instruction)
                n += 1
                continue
            wires[wire] = wires[inst]
    else:
        if "AND" in inst:
            a, b = inst.split(" AND ")
            if a == "1":
                if b not in wires:
                    instructions.append(instruction)
                    n += 1
                    continue
                wires[wire] = 1 & wires[b]
            elif a not in wires or b not in wires:
                instructions.append(instruction)
                n += 1
                continue
            else:
                wires[wire] = wires[a] & wires[b]
        elif "OR" in inst:
            a, b = inst.split(" OR ")
            if a not in wires or b not in wires:
                instructions.append(instruction)
                n += 1
                continue
            wires[wire] = wires[a] | wires[b]
        elif "LSHIFT" in inst:
            a, k = inst.split(" LSHIFT ")
            if a not in wires:
                instructions.append(instruction)
                n += 1
                continue
            wires[wire] = wires[a] << int(k)
        elif "RSHIFT" in inst:
            a, k = inst.split(" RSHIFT ")
            if a not in wires:
                instructions.append(instruction)
                n += 1
                continue
            wires[wire] = wires[a] >> int(k)
        elif "NOT" in inst:
            _, a = inst.split(" ")
            if a not in wires:
                instructions.append(instruction)
                n += 1
                continue
            wires[wire] = 65536 + ~wires[a]
    if n - i == 1 or "a" in wires:
        break

# ANSWER 2
print(wires["a"])
