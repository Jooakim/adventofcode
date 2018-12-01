with open('input', 'r') as f:
    inp = f.readline()
    inp = inp[:-1]
s = 0
for i,d in enumerate(inp):
    halfway_around = int(i+len(inp)/2)
    if d == inp[halfway_around%(len(inp))]:
        s += int(d)
print(s)
