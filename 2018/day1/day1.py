import pandas as pd
inp = [i[0] for i in pd.read_csv('input', header=None).values]
print(sum(inp))
seen = set()
cur = i = 0
while cur not in seen:
    seen.add(cur)
    cur += inp[i]
    i = (i + 1) % len(inp)
print(cur)


