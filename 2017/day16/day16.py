import pprint
def part_a(inp, size, positions=None):
    if positions is None:
        positions = list(range(size))

    for command in inp:
        move = command[0]
        if move == 's':
            spins = int(command[1:])
            tmp = positions[:-spins]
            positions[:spins] = positions[-spins:]
            positions[spins:] = tmp
        elif move == 'x':
            exchange = [int(x) for x in command[1:].split('/')]
            positions[exchange[0]], positions[exchange[1]] = \
                positions[exchange[1]], positions[exchange[0]]
        elif move == 'p':
            exchange = [positions.index(ord(x.lower()) - ord('a')) for x in command[1:].split('/')]
            positions[exchange[0]], positions[exchange[1]] = \
                positions[exchange[1]], positions[exchange[0]]
        else:
            raise Exception
    return positions



def main():
    with open('input') as f:
        inp = f.readlines()
    inp = inp[0].split(',')
    #inp = ['s1', 'x3/4', 'pe/b']
    size = 16
    positions = part_a(inp, size)
    l = [chr(positions[i]+97) for i in range(size)]
    print(''.join(l))
    positions = None
    s = set()
    for i in range(1000000000%60):
        positions = part_a(inp, size, positions=positions)
        # if str(positions) in s:
            # print(i)
            # break
        # else:
            # s.add(str(positions))

    l = [chr(positions[i]+97) for i in range(size)]
    print(''.join(l))



if __name__ == "__main__":
    main()
