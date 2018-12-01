
def solve():

    s = set()
    vals = {}
    childs = set()
    structure = {}
    with open('input','r') as f:
        for line in f.readlines():
            line = line.replace(',','')
            tmp = line.split()
            s.add(tmp[0])
            vals[tmp[0]] = int(tmp[1].replace('(', '').replace(')', ''))
            for t in tmp[3:]:
                childs.add(t)
                structure.setdefault(tmp[0], list()).append(t)
    root = s.difference(childs)
    root = root.pop()
    root = structure[root][0]
    root = structure[root][0]
    for child in structure[root]:
        queue = list()
        if child in structure:
            queue.extend(structure[child])
        val = vals[child]
        print('init', val)
        while len(queue) > 0:
            ele = queue.pop()
            val += vals[ele]
            if ele in structure:
                queue.extend(structure[ele])
        print(val)

solve()
    
