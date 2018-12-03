with open('input.txt') as f:
    s = f.readlines()
    alph = [[0 for x in range(26)] for y in  range(len(s[0]))]
    for row in s:
        for i in range(len(row)-1):
            alph[i][ord(row[i]) - ord('a')] += 1

    sol = ''
    for row in alph:
        m = 0
        for i in range(len(row)):
            if row[i] < row[m]:
                m = i
        sol += chr(ord('a') + m)

    print sol
            
