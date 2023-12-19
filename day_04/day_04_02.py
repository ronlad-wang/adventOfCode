import re
import sys
file_path = './day_04/input.txt'
file1 = open(file_path, 'r')
Lines = file1.readlines()

sum = 0

for line in Lines:
    matches = re.finditer(r"[0-9]+", line[9:])
    winning = []
    i = 0
    total_winning = 0
    for match in matches:
        if i < 10:
            winning.append(int(line[match.start() + 9:match.end() + 9]))
            i += 1
        else:
            if int(line[match.start() + 9:match.end() + 9]) in winning:
                total_winning += 1

    if(total_winning > 0):
        sum += 2**(total_winning-1)

print(sum)