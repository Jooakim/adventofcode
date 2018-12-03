with open('input', 'r') as f:
    a = [int(l) for l in f.readlines()]
dic = {}
pos = 0
tot = 0
while pos < len(a) and pos >= 0:
    instr = a[pos]
    offset = dic.get(pos, 0)
    instr += offset
    if instr >= 3:
        dic[pos] = dic.get(pos, 0)-1
    else:
        dic[pos] = dic.get(pos, 0)+1
    pos += instr
    tot += 1
print(tot)

