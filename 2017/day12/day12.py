def solve():
    graph = {}
    with open('input', 'r') as f:
        for line in f.readlines():
            tmp = line.split(' <-> ')
            node = tmp[0]
            l = list()
            for neighbor in tmp[1].split(', '):
                l.append(neighbor.strip())
            graph[node] = l

    q = list()
    q.extend('0')
    s = set()
    while len(q) > 0:
        tmp = q.pop()
        new_list = graph[tmp]
        for n in new_list:
            if n not in s:
                q.append(n)
        s.add(tmp)

    print(len(s))

def solve2():
    graph = {}
    with open('input', 'r') as f:
        for line in f.readlines():
            tmp = line.split(' <-> ')
            node = tmp[0]
            l = list()
            for neighbor in tmp[1].split(', '):
                l.append(neighbor.strip())
            graph[node] = l

    groups = 0
    graph2 = graph.copy()
    while len(graph2) > 0:
        q = list()
        q.append(next (iter (graph2.values()))[0])
        s = set()
        while len(q) > 0:
            tmp = q.pop()
            new_list = graph[tmp]
            for n in new_list:
                if n not in s:
                    q.append(n)
            s.add(tmp)
        groups += 1
        for n in s:
            graph2.pop(n)

    print(groups)

solve2()
