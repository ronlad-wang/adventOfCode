r = 12
g = 13
b = 14
import re
import sys
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
    power = 1
    max_blue = -sys.maxsize - 1
    max_red = -sys.maxsize - 1
    max_green = -sys.maxsize - 1

    for b in blue:
        x = re.findall("[0-9]+", b)
        num_blue = int(x[0])

        if max_blue < num_blue:
            max_blue = num_blue


    for r in red:
        x = re.findall("[0-9]+", r)
        num_red = int(x[0])

        if max_red < num_red:
            max_red = num_red


    for g in green:
        x = re.findall("[0-9]+", g)
        num_green = int(x[0])

        if max_green < num_green:
            max_green = num_green

    power = max_green * max_red * max_blue

    sum += power



    


print(sum)