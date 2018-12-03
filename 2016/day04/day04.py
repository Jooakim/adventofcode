import re
import operator


def checkValid(sorted_keys, check_sum):
    dic = dict(sorted_keys)
    for i in range(5):
        if dic.has_key(check_sum[i]) and (sorted_keys[i][0] == check_sum[i] or dic[sorted_keys[i][0]] == dic[check_sum[i]]):
            continue
        else:
            return False
    return True

valid = 0

def decrypt(word, nr_of_rotations):
    output = ''
    for c in word:
        tmp = ord(c) + nr_of_rotations 
        if tmp > ord('z'):
            tmp = ord('a') + (tmp - ord('z') - 1)
        output = output + chr(tmp)
    return output

with open('input.txt') as f:
    inp = f.readlines()
    for row in inp:
        a = row.split('-')
        keys = {}
        sentence = ''
        for col in a:
            if re.match('[a-z]', col):
                for c in col:
                    if keys.has_key(c):
                        keys[c] = keys[c] + 1
                    else:
                        keys[c] = 1
            else:
                section_id = int(''.join(s for s in col if s.isdigit()))
                check_sum = col[len(str(section_id))+1:len(col)-2]
                sorted_keys = sorted(keys.items(), key=operator.itemgetter(1), reverse=True)

                if checkValid(sorted_keys, check_sum):
                    for col2 in a[0:len(a)-2]:
                        sentence = sentence + decrypt(col2,section_id%26) + ' ' 
                    valid += section_id 
                    print sentence + ' ' + str(section_id)

print valid


