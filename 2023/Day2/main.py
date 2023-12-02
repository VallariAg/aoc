import re

TARGET = {
    "red": 12,
    "green": 13,
    "blue": 14,
}

f = open("input.txt", "r")

power_sum = 0
sum = 0
for line in f:
    blues = re.findall("\d+(?= blue)", line)
    blues = list(map(int, blues))
    red = re.findall("\d+(?= red)", line)
    red = list(map(int, red))
    green = re.findall("\d+(?= green)", line)
    green = list(map(int, green))
    game_id = re.findall("(?<=^Game )\d+", line)
    game_id = int(game_id[0])

    game_capacity = {
        "blue": max(blues + [0]),
        "red": max(red + [0]),
        "green": max(green + [0])
    }
    ok = 0
    for color, cap in (TARGET.items()):
        real_cap = game_capacity[color]
        if real_cap <= cap:
            ok += 1
    if ok == 3:
        sum += game_id
    power = 1
    for color, count in game_capacity.items():
        power *= count
    power_sum += power


print(sum)
print(power_sum)

