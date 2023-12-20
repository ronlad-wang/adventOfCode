import re
import math
file_path = './day_06/input.txt'
file1 = open(file_path, 'r')
Lines = file1.readlines()

times = re.finditer(r"[0-9]+", Lines[0])
distances = re.finditer(r"[0-9]+", Lines[1])

time_str = ""
dist_str = ""

for time in times:
    time_str += (Lines[0][time.start():time.end()])

for dist in distances:
    dist_str += (Lines[1][dist.start():dist.end()])



ret_val = 1


a = 1
b = -1 * int(time_str)
c = int(dist_str)

# calculating  the discriminant
dis = (b**2) - (4 * a*c)

# find two results
ans1 = math.ceil((-b-math.sqrt(dis))/(2 * a))
ans2 = math.floor((-b + math.sqrt(dis))/(2 * a))

# printing the results
print('The roots are')
print(ans1)
print(ans2)
print(ans2 - ans1 + 1)
ret_val *= (ans2 - ans1 + 1)
    


print(ret_val)