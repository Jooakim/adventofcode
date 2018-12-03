def solve():
    a = 618
    b = 814

    c = 2147483647

    factor_a = 16807
    factor_b = 48271

    eq = 0

    for i in range(40000000):
        a *= factor_a
        b *= factor_b 

        a = a%c
        b = b%c

        bin_a = bin(a)
        bin_b = bin(b)

        if bin_a[len(bin_a)-16:len(bin_a)] == bin_b[len(bin_b)-16:len(bin_b)]:
            eq += 1
    print(eq)

def solve2():
    a = 618
    b = 814

    c = 2147483647

    factor_a = 16807
    factor_b = 48271

    eq = 0

    for i in range(5000000):
        crit_a = False
        while not crit_a:
            a *= factor_a
            a = a%c

            crit_a = (a%4 == 0)

        crit_b = False
        while not crit_b:
            b *= factor_b 
            b = b%c

            crit_b = (b%8 == 0)


        bin_a = bin(a)
        bin_b = bin(b)

        if bin_a[len(bin_a)-16:len(bin_a)] == bin_b[len(bin_b)-16:len(bin_b)]:
            eq += 1
    print(eq)
                




solve2()
