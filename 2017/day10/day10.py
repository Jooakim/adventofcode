def solve():
    with open('input', 'r') as f:
        instr = f.readline().split(',')
    regs = [i for i in range(256)]
    skip_size = 0
    current_pos = 0

    for i in instr:
        i = int(i)
        end_pos = current_pos + i

        tmp_arr = regs + regs
        tmp = tmp_arr[current_pos:end_pos]
        tmp = tmp[::-1]
        regs[current_pos:min(end_pos, 256)] = tmp[:min(end_pos, 256-current_pos)]
        if (end_pos > 256):
            regs[0:end_pos-256] = tmp[256-current_pos:]

        current_pos = (end_pos + skip_size)%256
        skip_size += 1
    print(regs[0]*regs[1])

def solve2():
    with open('input', 'r') as f:

        instr = f.readline().strip()
    instr = '120,93,0,90,5,80,129,74,1,165,204,255,254,2,50,113'
    instr = [ord(i) for i in instr]
    print(len(instr))
    instr = instr+[17,31,73,47,23]
    print(instr)
    regs = [i for i in range(256)]
    skip_size = 0
    current_pos = 0

    for j in range(64):
        for i in instr:
            i = int(i)
            end_pos = current_pos + i

            tmp_arr = regs + regs
            tmp = tmp_arr[current_pos:end_pos]
            tmp = tmp[::-1]
            regs[current_pos:min(end_pos, 256)] = tmp[:min(end_pos, 256-current_pos)]
            if (end_pos > 256):
                regs[0:end_pos-256] = tmp[256-current_pos:]

            current_pos = (end_pos + skip_size)%256
            skip_size += 1
    print(regs)
    dense_hash = []
    for i in range(16):
        tmp = 0
        for j in range(16):
            tmp ^= regs[i*16+j]
        dense_hash.append(tmp)
    print(dense_hash)
    hex_hash = ''.join('{:02x}'.format(c) for c in dense_hash)
    print(hex_hash)



solve()
solve2()
