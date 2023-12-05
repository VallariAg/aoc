
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

print(maps.keys())

def get_dest_value(dest_map, curr_value):
    curr_value = int(curr_value)
    dest_value = curr_value
    for d_index, s_index, range_len in dest_map:
        d_index, s_index, range_len = int(d_index), int(s_index), int(range_len) 
        if curr_value >= s_index and curr_value < (s_index + range_len):
            diff = curr_value - s_index
            dest_value = d_index + diff
            break
    return dest_value


source_items = seeds
for i in range(maps_count):
    dest_items = []
    dest_map = maps[i]
    for item in source_items:
        dest_items += [get_dest_value(dest_map, item)]
    source_items = dest_items

print(min(source_items))
