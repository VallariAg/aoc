
f = open("input.txt", "r")


def print_matrix(mat):
    for i in mat:
        print(i)

DIRECTIONS = {
    "|": [(-1, 0), (1, 0)],
    "-": [(0, -1), (0, 1)],
    
    "L": [(-1, 0), (0, 1)],
    "J": [(-1, 0), (0, -1)],
    "F": [(1, 0), (0, 1)],
    "7": [(1, 0), (0, -1)],
    
    # ".": [(0, 0), (0, 0)],
}

matrix = []
dist_matrix = []
for line in f:
    matrix += [list(line.strip())]
    dist_matrix += [[0] * len(line.strip())]

# print_matrix(matrix)
# print_matrix(dist_matrix)
# dist_matrix = [[0] * len(matrix[0])] * len(matrix)

# animal_x, animal_y = 0, 0
# find animal position
def find_animal():
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == "S":
                return i, j
    return -1, -1

animal_x, animal_y = find_animal()

paths = [[], []]

def find_pipe_ends(x, y):
    value = matrix[x][y]
    if value == ".":
        return []
    n_connections = DIRECTIONS[value]
    connection_indexes = []
    for conn_x, conn_y in n_connections:
        connection_indexes += [(x + conn_x, y + conn_y)]
    return connection_indexes

visited = []
count = 0
# def get_other_ends(prev_x, prev_y, curr_x, curr_y, dist_matrix):
#     global visited
#     global count
# # for curr_x, curr_y in
#     count += 1
#     print(count)
#     if (curr_x, curr_y) in visited:
#         print("TURN DOWN FOR WHAT")
#     if curr_x < 0 or curr_y < 0 or curr_x >= len(matrix) or curr_y >= len(matrix[0]):
#         return 0
#     if matrix[curr_x][curr_y] == ".":
#         return 0
#     if matrix[curr_x][curr_y] == "S":
#         print("new S", prev_x, prev_y)
#         return (dist_matrix[prev_x][prev_y] + 1)
#     if dist_matrix[curr_x][curr_y] != 0:
#         return 0
#     pipe_ends = find_pipe_ends(curr_x, curr_y)
#     print((prev_x, prev_y), matrix[prev_x][prev_y], (curr_x, curr_y), matrix[curr_x][curr_y], pipe_ends)
#     if (prev_x, prev_y) in pipe_ends:
#         dist_matrix[curr_x][curr_y] = (dist_matrix[prev_x][prev_y] + 1)
#         other_end_ = set(pipe_ends) - set(list([(prev_x, prev_y)]))
#         other_end = list(other_end_)[0]
#         # print("printing...", other_end)
#         # print_matrix(dist_matrix)
#         visited += [(curr_x, curr_y)]
#         return get_other_ends(curr_x,  curr_y, other_end[0], other_end[1], dist_matrix)



prev_x, prev_y = animal_x, animal_y
for x, y in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
    neighbor_x, neighbor_y = animal_x + x, animal_y + y
    # ans = get_other_ends(animal_x, animal_y, neighbor_x, neighbor_y, dist_matrix)
    curr_x, curr_y = neighbor_x, neighbor_y

    count += 1
    # print(count)
    ans = 0
    while (curr_x, curr_y) != (animal_x, animal_y):
        if (curr_x, curr_y) in visited:
            # print("TURN DOWN FOR WHAT")
            break
        if curr_x < 0 or curr_y < 0 or curr_x >= len(matrix) or curr_y >= len(matrix[0]):
            # print("HWAT")
            break
        if matrix[curr_x][curr_y] == ".":
            # print("HWAT")
            break
        if matrix[curr_x][curr_y] == "S":
            # print("new S", prev_x, prev_y)
            ans = (dist_matrix[prev_x][prev_y] + 1)
            break
        if dist_matrix[curr_x][curr_y] != 0:
            # print("WHAAaa")
            break
        pipe_ends = find_pipe_ends(curr_x, curr_y)
        # print((prev_x, prev_y), matrix[prev_x][prev_y], (curr_x, curr_y), matrix[curr_x][curr_y], pipe_ends)
        if (prev_x, prev_y) in pipe_ends:
            # print("here")
            dist_matrix[curr_x][curr_y] = (dist_matrix[prev_x][prev_y] + 1)
            other_end_ = set(pipe_ends) - set(list([(prev_x, prev_y)]))
            other_end = list(other_end_)[0]
            visited += [(curr_x, curr_y)]
            prev_x, prev_y = curr_x,  curr_y
            curr_x,  curr_y = other_end[0], other_end[1]
        else:
            break
        ans = dist_matrix[prev_x][prev_y] + 1
        # print((prev_x, prev_y), matrix[prev_x][prev_y], (curr_x, curr_y), matrix[curr_x][curr_y], pipe_ends)

    if ans > 1:
        print("answer", ans / 2)
        break

# print("dist")
# print_matrix(dist_matrix)

closed_loop = []

for i in range(len(matrix)):
    s = ""
    for j in range(len(matrix[0])):
        if dist_matrix[i][j] > 0:
            s+= matrix[i][j]
        elif matrix[i][j] == "S":
            s += "7"
        elif matrix[i][j] == ".":
            s += "."
        else:
            s += " "
    closed_loop += [s]

count_inside = 0

for i in range(len(matrix)):
    verticals = 0
    last_vertical = "-"
    new = ""
    for j in range(len(matrix[0])):
        if closed_loop[i][j] in ". " and not (verticals % 2 == 0):
            count_inside += 1
            new += f'\033[0;32m█\033[0m'
        else:
            new += closed_loop[i][j]
        if closed_loop[i][j] == "7":
            if last_vertical == "L":
                last_vertical = "-"
                pass
            else:
                last_vertical = closed_loop[i][j]
                verticals += 1 
        elif closed_loop[i][j] == "J":
            if last_vertical == "F":
                last_vertical = "-"
                pass
            else:
                last_vertical = closed_loop[i][j]
                verticals += 1 
        elif closed_loop[i][j] in "|7FL":
            verticals += 1
            last_vertical = closed_loop[i][j]
    print(new.replace(".", " "), count_inside)
print("count_inside" , count_inside)



