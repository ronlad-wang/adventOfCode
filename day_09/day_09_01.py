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
    prev_starts = []
    matches = re.finditer(r"-?[0-9]+", line)
    line_vals = []
    for match in matches:
        line_vals.append(int(line[match.start():match.end()]))
        
    while not check_if_all_zeroes(line_vals):
        prev_starts.append(line_vals[0])
        temp_vals = [0] * (len(line_vals) - 1)
        for i in range(len(line_vals) - 1):
            temp_vals[i] = line_vals[i+1] - line_vals[i]
        line_vals = temp_vals
    print(line_vals)
    print(prev_starts)
    line_vals.append(0)

    for j in range(len(prev_starts)):
        temp = [0] * (len(line_vals) + 1)
        temp[0] = prev_starts[len(prev_starts) - 1 - j]
        for i in range(len(line_vals)):
            temp[i + 1] = temp[i] + line_vals[i]
        line_vals = temp
    
    print(line_vals)
    sum += line_vals[len(line_vals) - 1]

print(sum)
