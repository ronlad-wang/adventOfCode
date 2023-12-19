import re
import sys
file_path = './day_03/q1.txt'
file1 = open(file_path, 'r')
Lines = file1.readlines()
pattern = "[0-9]+"
sum = 0

for i in range(len(Lines)):
    line = Lines[i]
    #finditer is a great method that finds the location of every item in a String that matches the pattern
    #and returns a matchObject
    matches = re.finditer(pattern, line)
    for match in matches:
        s = match.start()
        e = match.end()
        has_neighbor = False
        #using these nested for loops we look at the adjacent characters
        for h in range(s, e):
            for j in range(-1, 2):
                for k in range(-1, 2):
                    #strange bug here - python apparently counts the new line character when calculating len(line)
                    #which caused me a lot of headache. I ended up hard coding the 140 but this could be fixed
                    #every line which is not the last line has length 141, which is 1 greater than what we want to
                    #consider.
                    if i + j < 0 or i + j >= len(Lines) or h + k < 0 or h + k >= 140:
                        continue
                    
                    #if we're not out of bounds, check if the adjacent tile is a special character,
                    #and that we have not already considered this current tile
                    if not re.match(r"[0-9.]", Lines[i + j][h + k]) and not has_neighbor:
                        print(Lines[i+j][h+k] + ", " + line[s:e] + ", "+ str(i + j) + ", " + str(h+k))
                        has_neighbor = True
                        sum += int(line[s:e])
        
        
print(sum)

