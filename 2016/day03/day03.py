def checkSides(x,y,z):
    return x+y>z and x+z>y and y+z>x
with open('input.txt') as f:
    inp = f.readlines()
    valid = 0
    for row in inp:
        x = row.split()
        if (checkSides(int(x[0]),int(x[1]),int(x[2]))):
            valid += 1
        
    print valid

    valid = 0
    stored = []
    a = []
    b = []
    c = []
    for row in inp:
        x = row.split()
        a.append(x[0])
        b.append(x[1])
        c.append(x[2])
        if len(a) == 3:
            if (checkSides(int(a[0]),int(a[1]),int(a[2]))):
                valid += 1
            if (checkSides(int(b[0]),int(b[1]),int(b[2]))):
                valid += 1
            if (checkSides(int(c[0]),int(c[1]),int(c[2]))):
                valid += 1
            a = []
            b = []
            c = []
        
        
    print valid
