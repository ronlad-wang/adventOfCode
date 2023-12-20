import re
import numpy
file_path = './day_09/input.txt'
file1 = open(file_path, 'r')
Lines = file1.readlines()

def check_if_all_zeroes(line_vals):
    for i in range(len(line_vals)):
        if not line_vals[i] == 0:
            return False
    return True
sum = 0
for line in Lines:
    prev_ends = []
    matches = re.finditer(r"-?[0-9]+", line)
    line_vals = []
    for match in matches:
        line_vals.append(int(line[match.start():match.end()]))
        
    while not check_if_all_zeroes(line_vals):
        prev_ends.append(line_vals[len(line_vals) - 1])
        temp_vals = [0] * (len(line_vals) - 1)
        for i in range(len(line_vals) - 1):
            temp_vals[i] = line_vals[i+1] - line_vals[i]
        line_vals = temp_vals
    print(line_vals)
    print(prev_ends)
    line_vals.append(0)

    for j in range(len(prev_ends)):
        temp = [0] * (len(line_vals) + 1)
        temp[len(temp) - 1] = prev_ends[len(prev_ends) - 1 - j]
        for i in range(len(line_vals)):
            temp[len(temp) - 2 - i] = temp[len(temp) - 1 - i] - line_vals[len(line_vals) - 1 - i]
        line_vals = temp
    
    print(line_vals)
    sum += line_vals[0]

print(sum)
