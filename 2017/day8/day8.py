def solve():
    max_value = 0
    with open('input', 'r') as f:
        regs = {}
        for line in f.readlines():
            tmp = line.split()
            reg = tmp[0]
            instr = tmp[1]
            instr_val = int(tmp[2])
            cond_reg = tmp[4]
            cond = tmp[5]
            cond_val = int(tmp[6])

            cond_reg_val = regs.get(cond_reg, 0)

            if (cond == '>' and cond_reg_val > cond_val):
                pass
            elif (cond == '<' and cond_reg_val < cond_val):
                pass
            elif (cond == '>=' and cond_reg_val >= cond_val):
                pass
            elif (cond == '<=' and cond_reg_val <= cond_val):
                pass
            elif (cond == '!=' and cond_reg_val != cond_val):
                pass
            elif (cond == '==' and cond_reg_val == cond_val):
                pass
            else:
                continue

            if instr == 'dec':
                regs[reg]  = regs.get(reg, 0) - instr_val
            elif instr == 'inc':
                regs[reg]  = regs.get(reg, 0) + instr_val
            else:
                print(instr)
            max_value = max(max(regs.values()), max_value)
    print(max_value)
            


solve()
