import re
sum = 0

file1 = open('./data/trebuchet.txt', 'r')
lines = file1.readlines()

for l in lines:
    f = re.search(r'[0-9]', l).group()
    l = re.findall(r'[0-9]', l)[-1]
    num = int(f) * 10 + int(l)

    sum = sum + num

print(sum)