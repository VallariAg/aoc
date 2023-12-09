
f = open("input.txt", "r")

report = []
for line in f:
    line = [int(num) for num in line.strip().split(" ")]
    report += [line]

def get_next_diff(arr):
    new_array = []
    for i in range(len(arr)-1):
        new_array += [arr[i+1] - arr[i]]
    return new_array

predictions = []
for line in report:
    next_diff = line
    diff_collection = [next_diff]
    while set(next_diff) != set([0]):
        next_diff = get_next_diff(next_diff)
        diff_collection += [next_diff]

    base = 0
    for i in list(reversed(range(len(diff_collection) - 1))):
        # base = diff_collection[i][-1] + base # PART 1
        base = diff_collection[i][0] - base # PART 2
    predictions += [base]

print(predictions)
print(sum(predictions))