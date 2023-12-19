import re
import sys
file_path = './day_03/q1.txt'
file1 = open(file_path, 'r')
Lines = file1.readlines()
pattern = "[0-9]+"
sum = 0

for i in range(len(Lines)):
    line = Lines[i]
    matches = re.finditer(pattern, line)
    for match in matches:
        s = match.start()
        e = match.end()
        has_neighbor = False
        for h in range(s, e):
            for j in range(-1, 2):
                for k in range(-1, 2):
                    if i + j < 0 or i + j >= len(Lines) or h + k < 0 or h + k >= 140:
                        continue
                    
                    if not re.match(r"[0-9.]", Lines[i + j][h + k]) and not has_neighbor:
                        print(Lines[i+j][h+k] + ", " + line[s:e] + ", "+ str(i + j) + ", " + str(h+k))
                        has_neighbor = True
                        sum += int(line[s:e])
        
        
print(sum)

