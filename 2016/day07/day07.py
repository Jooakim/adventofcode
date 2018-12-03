import re

def is_palindrom(s):
    return s == s[::-1] and s[0] != s[1]

def has_palindrom(s):
    for i in range(len(s)-3):
        if (is_palindrom(s[i:i+4])):
            return True
    return False


with open('input.txt') as f:
    s = f.readlines()
    count = 0
    for row in s:

        row = row[0:len(row)-1]
        test = re.split('[\[\]]', row)
        tls = False
        for i in range(len(test)):
            if (i%2 == 0 and has_palindrom(test[i])):
                tls = True
            elif (i%2 == 1 and has_palindrom(test[i])):
                tls = False
                break

        if tls:
            count += 1

    print count
