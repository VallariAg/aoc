
from collections import defaultdict

f = open("input.txt", "r")

maps_count = 7
seeds = ""
maps = defaultdict(list)
map_index = -1
with open('input.txt') as f:
    seeds = f.readline()
    for line in f:
        if line.strip() == "":
            map_index += 1
            f.readline()
        else:
            dest_start, source_start, range_len = line.strip().split(" ")
            maps[map_index] += [[dest_start, source_start, range_len]]
seeds = seeds[6:].strip().split(" ")

seed_ranges = []
for i in range(0, len(seeds), 2):
    seed_ranges += [[int(seeds[i]), int(seeds[i])+int(seeds[i+1])]]

def get_dest_value(dest_map, curr_value):
    curr_value = int(curr_value)
    dest_value = curr_value
    for d_index, s_index, range_len in dest_map:
        s_index, d_index, range_len = int(d_index), int(s_index), int(range_len) 
        if curr_value >= s_index and curr_value < (s_index + range_len):
            diff = curr_value - s_index
            dest_value = d_index + diff
            break
    return dest_value


for loc in range(0, 100000000):
    item = loc
    for i in [6,5,4,3,2,1,0]:
        dest_map = maps[i]
        item = get_dest_value(dest_map, item)
    for start, end  in seed_ranges:
        if item >= int(start) and item < int(end):
            print("found seed at ", loc)
            break
    if loc % 10000 == 0:
        print("loc: ", loc)

# print(min(source_items))
