nums = [ "zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
digs = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
f = open("input.txt", "r")
sum = 0
for line in f:
    first, last = "", ""
    for char_index in range(len(line)):
        if line[char_index] in "1234567890":
            if not first:
                first = line[char_index]
            last = line[char_index]
        for index, i in enumerate(nums):
            char_index_ = char_index + 1
            if i[0] == line[char_index]:
                nums_index = 1
                while nums_index <= len(i):
                    if i[nums_index - 1] != line[char_index_ - 1]:
                        char_index_ = char_index + 1
                        break
                    nums_index += 1 
                    char_index_ += 1
                if (nums_index) == (char_index_ - char_index):
                    char_index = char_index_
                    if not first:
                        first = digs[index]
                    last = digs[index]
                    break  
    # print(f"first {first}")        
    # print(f"last {last}")             
    code = first + last 
    # print(f"code {code}")             
    sum += int(code)

print(sum)


