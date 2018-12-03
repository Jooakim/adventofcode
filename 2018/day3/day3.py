claims = [claim.strip().split('@')[1] for claim in open('input')]
rects = dict()
ids = dict()
potentials = set(range(len(claims)))
for i, claim in enumerate(claims):
    x, y = map(int, claim.split(':')[0].split(','))
    width, height = map(int, claim.split(':')[1].split('x'))
    squares = [(x1, y1) for x1 in range(x, x + width)
               for y1 in range(y, y + height)]
    for square in squares:
        if square in ids:
            if i in potentials:
                potentials.remove(i)
            if ids[square] in potentials:
                potentials.remove(ids[square])
        else:
            ids[square] = i
        val = rects.get(square, 0)
        val += 1
        rects[square] = val
print(sum([1 for k, v in rects.items() if v >= 2]))
print(potentials.pop() + 1)
