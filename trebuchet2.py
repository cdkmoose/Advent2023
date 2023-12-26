import re
import sys

sum = 0

digits = {
    'one': 1, 'two': 2, 'three': 3, 'four': 4, "five":5, "six": 6, "seven":7,"eight":8, "nine":9
}


def get_first_num(s):
    
    f = re.search(r'[0-9]', s)
    if f == None:
        digit_index = sys.maxsize
    else:
        digit_index = f.start()

    fres = re.findall(r'one|two|three|four|five|six|seven|eight|nine', s)

    if len(fres) == 0:
        string_index = sys.maxsize
    else:
        fs = fres[0]
        string_index = s.find(fs)

    if (digit_index < string_index):
        return int(f.group())
    else:
        return digits[fs]


def get_last_num(s):
    lres = re.findall(r'[0-9]', s)
    if len(lres) == 0:
        digit_index = -1
    else:
        l = lres[-1]
        digit_index = s.rfind(l)

    # Find all occurrences of the substring
    lres = re.findall(r'(?=(one|two|three|four|five|six|seven|eight|nine))', s)

    if len(lres) == 0:
        string_index = -1
    else:
        ls = lres[-1]
        string_index = s.rfind(ls)

    if(digit_index > string_index):
        return int(l)
    else: 
        return digits[ls]


file1 = open('./data/trebuchet.txt', 'r')
lines = file1.readlines()
#lines = [ "chthreeone9eightoneshlgndnrjoneightcs", "two1nine", "eightwothree", "abcone2threexyz", "xtwone3four", "4nineeightseven2", "zoneight234", "7pqrstsixteen"]

for l in lines:
    first = get_first_num(l)

    last = get_last_num(l)

    num = int(first) * 10 + int(last)

    print(l + " : " + str(num))

    sum = sum + num

print(sum)

    

