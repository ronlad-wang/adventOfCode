r = 12
g = 13
b = 14
import re
file_path = './day_02/q1.txt'
file1 = open(file_path, 'r')
Lines = file1.readlines()

sum = 0
for line in Lines:
    line_id = 0
    if line[6] == ':':
        line_id = line[5]
    elif line[7] == ':':
        line_id = int(line[5]) * 10 + int(line[6])
    else:
        line_id = int(line[5]) * 100 + int(line[6]) * 10 + int(line[7])
    blue = re.findall("[0-9]+ blue", line)
    red = re.findall("[0-9]+ red", line)
    green = re.findall("[0-9]+ green", line)
    found_issue = False
    
    if not found_issue:
        for b in blue:
            x = re.findall("[0-9]+", b)
            num_blue = int(x[0])
            if num_blue > 14:
                found_issue = True
                break

    if not found_issue:
        for r in red:
            x = re.findall("[0-9]+", r)
            num_red = int(x[0])
            if num_red > 12:
                found_issue = True
                break

    if not found_issue:
        for g in green:
            x = re.findall("[0-9]+", g)
            num_green = int(x[0])
            if num_green > 13:
                found_issue = True
                break

    if not found_issue:
        print(int(line_id))
        sum += int(line_id)
    


print(sum)