import math


MAP = {}
LR_instructions = ""
with open('input.txt') as f:
    LR_instructions = f.readline().strip()
    for line in f:
        if len(line) > 3:
            a, l, r = line[0:3], line[7:10], line[12:15]
            MAP[a] = [l, r]


# find paths ending with A
paths = []
for i in MAP:
    if i[-1] == "A":
        paths += [i]

hop = 0
LR_pointer = 0
reached = []

while len(reached) != len(paths):
    hop += 1
    LorR = LR_instructions[LR_pointer]
    second_pointer = 0
    if LorR == "L":
        second_pointer = 0
    elif LorR == "R":
        second_pointer = 1
    else:
        print("how did we come here")
    for i, name in enumerate(paths):
        paths[i] = MAP[name][second_pointer]
        if paths[i][-1] == "Z":
            reached += [hop]
    if LR_pointer == len(LR_instructions) - 1:
        LR_pointer = 0
    else:
        LR_pointer += 1
    if hop % 100000 == 0:
        print(hop, paths)
    
    
# print(hop)
# print(reached)
print(math.lcm(*reached))
