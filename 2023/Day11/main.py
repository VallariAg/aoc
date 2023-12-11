
f = open("input.txt", "r")
def print_uni(universe):
    for i in universe:
        print(i)

count = 0
univserse = []
expanded_universe = []
galaxies = {}
empty_rows, empty_cols = [], []
for n, line in enumerate(f):
    if set(line.strip()) == set(["."]):
        expanded_universe += [line.strip()]
        expanded_universe += [line.strip()]
        empty_rows += [n]
    else:
        expanded_universe += [line.strip()]
    univserse += [line.strip()]


def is_col_empty(col_no):
    for row in range(len(univserse)):
        if univserse[row][col_no] == "#":
            return False
    return True

expanded_universe_2 = [""] * len(expanded_universe)
for col in range(len(univserse[0])):
    is_empty = is_col_empty(col)
    if is_empty:
        empty_cols += [col]
        for row in range(len(expanded_universe)):
            expanded_universe_2[row] += expanded_universe[row][col:col +1] + "."
    else:
        for row in range(len(expanded_universe)):
            expanded_universe_2[row] += expanded_universe[row][col:col +1]


multiple = 1000000

for i in range(len(univserse)):
    for j in range(len(univserse[0])):
        if univserse[i][j] == "#":
            count += 1
            galaxies[count] = (i, j)

distances = []
sum_ = 0
new_galaxyies = {}
for g in galaxies:
    print(g)
    for g2 in galaxies:
        if g!= g2:
            g_row, g_col = galaxies[g][0], galaxies[g][1]
            g2_row, g2_col = galaxies[g2][0], galaxies[g2][1]
            g_row_, g_col_ = g_row, g_col
            g2_row_, g2_col_ = g2_row, g2_col
            for i in empty_cols:
                if i < g_col:
                    g_col_ += multiple - 1
                if i < g2_col:
                    g2_col_ += multiple - 1
            for j in empty_rows:
                if j < g_row:
                    g_row_ += multiple -1
                if j < g2_row:
                    g2_row_ += multiple -1
            print(g, (g_row_, g_col_), g2, (g2_row_, g2_col_))
            dist = abs(g_col_ - g2_col_) + abs(g_row_ - g2_row_)
            sum_ += dist
            distances += [(g, g2, dist)]
            new_galaxyies[g] = (g_row_, g_col_)
            new_galaxyies[g2] = (g2_row_, g2_col_)
            
# print(galaxies)
# print(new_galaxyies)
# print(empty_cols)
# print(empty_rows)
# print(distances)
# print(sum_)
print(sum_ / 2)


# print(galaxies)

