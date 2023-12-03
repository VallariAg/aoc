import re


f = open("input.txt", "r")


def is_symbol(i1, i2, num):
    global gears
    global gear_ratios
    if i1 >= 140 or i2 >= 140 or i1 <0 or i2 < 0:
        return False
    char = input_2d[i1][i2]
    if char == "*":
        for gear in gears:
            a, b, val = gear[0], gear[1], gear[2]
            if a == i1 and b == i2:
                gear_ratios += [int(val) * int(num)]
        gears += [[i1, i2, num]]
    return char not in "1234567890."

def is_machine_part(s_index, e_index, line_no, num):
    length = e_index - s_index
    is_part = False
    for i in range(length):
        curr_index = s_index + i
        top = [line_no - 1, curr_index]
        bottom = [line_no + 1, curr_index]
        right = [line_no, curr_index + 1]
        left = [line_no, curr_index - 1]
        top_right = [line_no - 1, curr_index + 1]
        top_left = [line_no - 1, curr_index - 1]
        bottom_left = [line_no + 1, curr_index - 1]
        bottom_right = [line_no + 1, curr_index + 1]
        for i in [top, bottom, right, left, top_left, top_right, bottom_left, bottom_right]:
            if is_symbol(i[0], i[1], num):
                is_part = True
                break
        if is_part:
            break
    return is_part

input_2d = []
row_len, rows_num = 140, 140
gear_ratios = []
gears = []

f = open("input.txt", "r")
for line in f:
    input_2d += [line]

sum = 0
for line_no, line in enumerate(input_2d):
    for match in re.finditer('\d+', line):
        num_value = match.group()
        start_index = match.start()
        end_index = match.end()
        if is_machine_part(start_index, end_index, line_no, num_value):
            sum += int(num_value)

print(sum)

gear_sum = 0
for i in gear_ratios:
    gear_sum += i
print(gear_sum)
