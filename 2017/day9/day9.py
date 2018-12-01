import re

def solve():
    with open('input', 'r') as f:
        stream = f.readline()
    groups = list()
    stream = re.sub('[!].', '', stream)
    val = 0
    garbage = False
    nr_of_garbage = 0
    for ch in stream:
        if not garbage and ch == '<':
            garbage = True
            continue
        elif ch == '>':
            garbage = False

        if not garbage:
            if ch == '{':
                groups.append('{')
            elif ch == '}':
                val += len(groups)
                groups.pop()
        else:
            nr_of_garbage += 1
    print(val)
    print(nr_of_garbage)


solve()
