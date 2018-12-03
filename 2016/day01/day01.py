#!/usr/bin/env python

import sys

inp='L5, R1, R3, L4, R3, R1, L3, L2, R3, L5, L1, L2, R5, L1, R5, R1, L4, R1, R3, L4, L1, R2, R5, R3, R1, R1, L1, R1, L1, L2, L1, R2, L5, L188, L4, R1, R4, L3, R47, R1, L1, R77, R5, L2, R1, L2, R4, L5, L1, R3, R187, L4, L3, L3, R2, L3, L5, L4, L4, R1, R5, L4, L3, L3, L3, L2, L5, R1, L2, R5, L3, L4, R4, L5, R3, R4, L2, L1, L4, R1, L3, R1, R3, L2, R1, R4, R5, L3, R5, R3, L3, R4, L2, L5, L1, L1, R3, R1, L4, R3, R3, L2, R5, R4, R1, R3, L4, R3, R3, L2, L4, L5, R1, L4, L5, R4, L2, L1, L3, L3, L5, R3, L4, L3, R5, R4, R2, L4, R2, R3, L3, R4, L1, L3, R2, R1, R5, L4, L5, L5, R4, L5, L2, L4, R4, R4, R1, L3, L2, L4, R3'

inp = inp.split(', ')



def sol(isSecondTask):
    global inp
    x = 0
    y = 0
    direction = 0 + 1j
    pos = {}
    for s in inp:
        if s[0] == 'R':
            direction *= -1j
        else:
            direction *= 1j
        for i in range(1, int(s[1::])+1):
            x += direction.real
            y += direction.imag
            if (isSecondTask):
                if pos.has_key((x,y)):
                    print (abs(x) + abs(y))
                    sys.exit(0)
                pos[(x,y)] = 1
    print (abs(x) + abs(y))
sol(False)
sol(True)
