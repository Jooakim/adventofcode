import copy
inp_list = [c for line in open('input') for c in line.strip()]
# inp_list = [c for c in 'dabAcCaCBAcCcaDA']
abc = [chr(ord('a') + i) for i in range(ord('z') - ord('a') + 1)]


def react_inp(inp):
    reaction = True
    while reaction:
        reaction = False
        indexes = set()
        for i in range(0, len(inp) - 1):
            a = inp[i]
            b = inp[i + 1]
            if (a.isupper() and b.islower() and a.lower() == b.lower()) or (
                    b.isupper() and a.islower() and a.lower() == b.lower()):
                if i in indexes: #  ugly hack
                    continue
                indexes.add(i)
                indexes.add(i + 1)
                reaction = True
        for index in sorted(indexes, reverse=True):
            del inp[index]
    return len(inp)


print(react_inp(copy.copy(inp_list)))
res = len(inp_list)
for c in abc:
    inp = [x for x in inp_list if x.lower() != c]
    res = min(react_inp(inp), res)
print(res)
