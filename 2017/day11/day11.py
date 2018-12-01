def solve():
    with open('input', 'r') as f:
        stream = f.readline().strip()

    x = 0
    y = 0
    
    m = 0
    for instr in stream.split(','):
        if instr == 'se':
            x += 1
            y -= 1
        elif instr == 'ne':
            x += 1
            y += 1
        elif instr == 'n':
            y += 1
        elif instr == 'nw':
            x -= 1
            y += 1
        elif instr == 'sw':
            x -= 1
            y -= 1
        elif instr =='s':
            y -= 1
        else:
            print('fail')
        m = max(m, max(x,y))
    x = abs(x)
    y = abs(y)

    print('final', max(x,y))
    print('max', m)

    

solve()
