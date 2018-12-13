import dataclasses
inp = [list(map(int, inp.strip().split())) for inp in open('input')][0]

# inp = [2, 3, 0, 3, 10, 11, 12, 1, 1, 0, 1, 99, 2, 1, 1, 2]


def solve(inp):
    children_in_line = []
    metadata_in_line = []
    pos = 0

    all_nodes = []
    root_nodes = []

    while pos < len(inp):
        if children_in_line and children_in_line[-1] == 0:
            children_in_line.pop()
            node = root_nodes.pop()
            metadata = metadata_in_line.pop()
            node.metadata.extend(inp[pos:pos+metadata])
            pos += metadata
        else:
            if children_in_line:
                children_in_line[-1] -= 1
            child = inp[pos]
            metadata = inp[pos + 1]
            node = Node(list(), list())
            all_nodes.append(node)
            if root_nodes:
                root_nodes[-1].childs.append(node)
            root_nodes.append(node)

            children_in_line.append(child)
            metadata_in_line.append(metadata)

            pos += 2
    return all_nodes

@dataclasses.dataclass
class Node:
    childs: list
    metadata: list

    def calculate_metadata(self):
        if not self.childs:
            return sum(self.metadata)

        return sum(self.childs[i-1].calculate_metadata()
                   for i in self.metadata if i <= len(self.childs))


nodes = solve(inp)
print(sum([sum(c.metadata) for c in nodes]))
print(nodes[0].calculate_metadata())
