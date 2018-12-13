inp = [list(map(int, inp.strip().split())) for inp in open('input')][0]

# inp = [2, 3, 0, 3, 10, 11, 12, 1, 1, 0, 1, 99, 2, 1, 1, 2]


def solve(inp):
    children_in_line = []
    metadata_in_line = []
    pos = 0
    total_metadata = []

    while pos < len(inp):
        if children_in_line and children_in_line[-1] == 0:
            children_in_line.pop()
            metadata = metadata_in_line.pop()
            total_metadata.extend(inp[pos:pos + metadata])
            pos += metadata
        else:
            if children_in_line:
                children_in_line[-1] -= 1
            child = inp[pos]
            metadata = inp[pos + 1]
            children_in_line.append(child)
            metadata_in_line.append(metadata)

            pos += 2
    return total_metadata


metadata = solve(inp)
print(sum(metadata))
