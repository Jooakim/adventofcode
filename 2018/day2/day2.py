from collections import Counter
import difflib

inp = [s.strip() for s in open('input')]
#inp = ['abcde', 'fghij', 'klmno', 'pqrst', 'fguij', 'axcye', 'wvxyz']
counts = [Counter(s) for s in inp]
twos = threes = 0
for count in counts:
    if any(v == 2 for k, v in count.items()):
        twos += 1
    if any(v == 3 for k, v in count.items()):
        threes += 1
print(twos, threes, twos * threes)

common = []
diff = []
for i, s in enumerate(inp):
    close = difflib.get_close_matches(s, inp[i+1:], n=1, cutoff=1-1/len(s))
    if close:
        for j, c in enumerate(close[0]):
            if c == s[j]:
                common.append(c)
            else:
                diff.append((j,c))
        break
print(''.join(common))
print(diff)
