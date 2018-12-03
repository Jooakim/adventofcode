def solve(allowedKeys, x, y):
    sol = []
    with open('input.txt') as f:
        inp = f.readlines()
        for row in inp:
            for c in row:
                if c == 'L':
                    mov = (-1,0)
                elif c == 'R':
                    mov = (1,0)
                elif c == 'D':
                    mov = (0,1)
                elif c == 'U':
                    mov = (0,-1)
                else:
                    continue

                if (x+mov[0] > -1 and x+mov[0] < len(allowedKeys[0]) and 
                    y+mov[1] > -1 and y+mov[1] < len(allowedKeys)):
                    if allowedKeys[y+mov[1]][x+mov[0]] != 0:
                        x += mov[0]
                        y += mov[1]
            sol.append(allowedKeys[y][x])
    print sol

allowedKeys = [[0 for i in range(3)] for j in range(3)]
allowedKeys[0][0] = '1'
allowedKeys[0][1] = '2'
allowedKeys[0][2] = '3'
allowedKeys[1][0] = '4'
allowedKeys[1][1] = '5'
allowedKeys[1][2] = '6'
allowedKeys[2][0] = '7'
allowedKeys[2][1] = '8'
allowedKeys[2][2] = '9'

solve(allowedKeys, 1,1)

allowedKeys = [[0 for i in range(5)] for j in range(5)]
allowedKeys[0][2] = '1'
allowedKeys[1][1] = '2'
allowedKeys[1][2] = '3'
allowedKeys[1][3] = '4'
allowedKeys[2][0] = '5'
allowedKeys[2][1] = '6'
allowedKeys[2][2] = '7'
allowedKeys[2][3] = '8'
allowedKeys[2][4] = '9'
allowedKeys[3][1] = 'A'
allowedKeys[3][2] = 'B'
allowedKeys[3][3] = 'C'
allowedKeys[4][2] = 'D'

solve(allowedKeys,2,2)
            
            
