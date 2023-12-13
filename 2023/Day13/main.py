from collections import defaultdict
f = open("input.txt", "r")
def print_uni(universe):
    for i in universe:
        for j in i:
            print(j)


def cont_index(line):
    same = []
    for i, char in enumerate(line):
        if i> 0 and line[i-1] == line[i]:
            same += [i]
    return same

def is_one_off_row(line1, line2):
    count = 0
    for i in range(len(line1)):
        if line1[i] == line2[i]:
            count += 1
    return count == (len(line1)) - 1

patterns = [[]]

cont_rows = [[]]
row_no = 0
cont_cols = [defaultdict(int)]
one_off_rows = [[]]
for n, line in enumerate(f):
    if not line.strip():
        patterns += [[]]
        cont_rows += [[]]
        one_off_rows += [[]]
        cont_cols += [defaultdict(int)]
        row_no = 0
    else:
        row_no += 1
        for i in cont_index(line.strip()):
            cont_cols[-1][i] += 1
        if patterns[-1] and patterns[-1][-1] == line.strip():
            cont_rows[-1] += [row_no-1] # index
        elif patterns[-1] and is_one_off_row(patterns[-1][-1], line.strip()):
            one_off_rows[-1] += [row_no-1] # index
        patterns[-1] += [line.strip()]

patterns_answer = [[]] * len(patterns)

col_sep = []
row_sep = []

def get_row_sep(cont_rows):
    row_sep_ = []
    for p_no, pattern in enumerate(patterns):
        for i in cont_rows[p_no]:
            above, below = i-2, i+1
            is_mirror = True
            while (above >= 0 and below < len(pattern)):
                if pattern[above] != pattern[below]:
                    is_mirror = False 
                    break
                above += -1
                below += 1
            if is_mirror:
                row_sep_ += [i]
                patterns_answer[p_no] = [p_no, "row", i]
    return row_sep_

def get_one_off_row_sep(one_off_rows, cont_rows):
    global patterns_answer
    pattern_ans = defaultdict(list)
    row_sep_ = []
    for p_no, pattern in enumerate(patterns):
        for i in one_off_rows[p_no]:
            above, below = i-2, i+1
            is_mirror = True
            while (above >= 0 and below < len(pattern)):
                if pattern[above] != pattern[below]:
                    is_mirror = False 
                    break
                above += -1
                below += 1
            if is_mirror:
                row_sep_ += [i]
                if not (patterns_answer[p_no][1] == "row" and patterns_answer[p_no][2] == i):
                    pattern_ans[p_no] += [i]

    for p_no, pattern in enumerate(patterns):
        for i in cont_rows[p_no]:
            above, below = i-2, i+1
            is_mirror = True
            one_off_done = False
            while (above >= 0 and below < len(pattern)):
                if not one_off_done and is_one_off_row(pattern[above], pattern[below]):
                    one_off_done = True
                    above += -1
                    below += 1
                    continue
                if pattern[above] != pattern[below]:
                    is_mirror = False 
                    break
                above += -1
                below += 1
            if is_mirror:
                row_sep_ += [i]
                if not (patterns_answer[p_no][1] == "row" and patterns_answer[p_no][2] == i):
                    pattern_ans[p_no] += [i]
    return pattern_ans

def get_col_sep(cont_cols):
    col_sep_ = []
    for p_no, pattern in enumerate(patterns):
        mirrored_cols = []
        same_cols = cont_cols[p_no]
        for i, count in same_cols.items():
            if count == len(pattern):
                mirrored_cols += [i]
        for i in mirrored_cols:
            left, right = i-2, i+1
            is_mirror = True
            while (left >= 0 and right < len(pattern[0])):
                col_match = True
                for row in pattern:
                    if row[right] != row[left]:
                        col_match = False
                        break
                if not col_match:
                    is_mirror = False
                right += 1
                left -= 1
            if is_mirror:
                col_sep_ += [i]
                patterns_answer[p_no] = [p_no, "column", i]
    return col_sep_

def get_one_off_col_sep(cont_cols):
    pattern_ans = defaultdict(list)
    col_sep_ = []
    for p_no, pattern in enumerate(patterns):
        one_off_cols = []
        same_cols = cont_cols[p_no]
        for i, count in same_cols.items():
            if count == len(pattern)-1:
                one_off_cols += [i]
        for i in one_off_cols:
            left, right = i-2, i+1
            is_mirror = True
            while (left >= 0 and right < len(pattern[0])):
                col_match = True
                for row in pattern:
                    if row[right] != row[left]:
                        col_match = False
                        break
                if not col_match:
                    is_mirror = False
                right += 1
                left -= 1
            if is_mirror:
                col_sep_ += [i]
                if not (patterns_answer[p_no][1] == "column" and patterns_answer[p_no][2] == i):
                    pattern_ans[p_no] += [i]

    for p_no, pattern in enumerate(patterns):
        mirrored_cols = []
        same_cols = cont_cols[p_no]
        one_off_done = False
        for i, count in same_cols.items():
            if count == len(pattern):
                if count == len(pattern)-1:
                    one_off_done = True
                mirrored_cols += [i]
        for i in mirrored_cols:
            left, right = i-2, i+1
            is_mirror = True
            one_off_done = False
            while (left >= 0 and right < len(pattern[0])):
                col_match = True
                for row in pattern:
                    if not one_off_done and row[right] != row[left]:
                        one_off_done = True
                        continue
                    if row[right] != row[left]:
                        col_match = False
                        break
                if not col_match:
                    is_mirror = False
                right += 1
                left -= 1
            if is_mirror:
                col_sep_ += [i]
                if not (patterns_answer[p_no][1] == "column" and patterns_answer[p_no][2] == i):
                    pattern_ans[p_no] += [i]
    return pattern_ans


row_sep = get_row_sep(cont_rows)
col_sep = get_col_sep(cont_cols)

print(patterns_answer)
part1 = sum(col_sep) + (100* sum(row_sep))
print(part1)
print("----------")
# PART 2

row_sep_2 = (get_one_off_row_sep(one_off_rows, cont_rows))
print(row_sep_2)
cols_sep_2 = get_one_off_col_sep(cont_cols)
print("cols:")
print(cols_sep_2)


rows_sum = 0
for i in row_sep_2.values():
    rows_sum += i[0]

cols_sum = 0
for i in cols_sep_2.values():
    cols_sum += i[0]

part2 = (rows_sum * 100) + cols_sum
print(part2)