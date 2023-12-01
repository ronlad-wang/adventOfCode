file_path = './day_01/q1.txt'
file1 = open(file_path, 'r')
Lines = file1.readlines()

def checkIfNextCharsEqualsInt(s, i):
    numbers = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    for j in range(len(numbers)):
        number = numbers[j]
        if i + len(number) <= len(s):
            if s[i:len(number) + i] == number:
                return j
    return -1


sum = 0
for line in Lines:
    first = -1
    last = -1
    for i in range(len(line)):
        if line[i].isdigit():
            if first == -1:
                first = line[i]
            last = line[i]
        
        string_num = checkIfNextCharsEqualsInt(line, i)
        if string_num != -1:
            if first == -1:
                first = string_num
            last = string_num
        
    combined = str(first) + str(last)
    sum += int(combined)




print(sum)