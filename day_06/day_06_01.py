import re
import math
file_path = './day_06/input.txt'
file1 = open(file_path, 'r')
Lines = file1.readlines()

times = re.finditer(r"[0-9]+", Lines[0])
distances = re.finditer(r"[0-9]+", Lines[1])

time_dist = []
i = 0
for time in times:
    time_dist.append([])
    time_dist[i].append(Lines[0][time.start():time.end()])
    i+=1
i = 0
for dist in distances:
    time_dist[i].append(Lines[1][dist.start():dist.end()])
    i+=1

print(time_dist)
sum = 1

for t_d in time_dist:
    a = 1
    b = -1 * int(t_d[0])
    c = int(t_d[1])

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
    sum *= (ans2 - ans1 + 1)
    


print(sum)