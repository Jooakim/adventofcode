class SecurityLayer():
    def __init__(self, gate, layer_range):
        self.gate = gate
        self.layer_range = layer_range
        self.position = 0
        self.update_dir = -1

    def reset(self):
        self.position = self.save_pos
        self.update_dir = self.save_dir

    def move(self):
        if self.position == (self.layer_range - 1) or self.position == 0:
            self.update_dir *= -1
        self.position += self.update_dir

    def save(self):
        self.save_pos = self.position
        self.save_dir = self.update_dir


def solve():
    layers = []
    packet = 0
    with open('input', 'r') as f:
        for instr in f.readlines():
            tmp = instr.split(': ')
            layer = SecurityLayer(int(tmp[0]), int(tmp[1]))
            layers.append(layer)
    cost = 0
    while packet < 99:
        packet += 1
        for layer in layers:
            layer.move()
            if layer.gate == packet and layer.position == 0:
                cost += layer.gate*layer.layer_range
    print(cost)

def solve2():
    layers = []
    packet = 0
    with open('input', 'r') as f:
        for instr in f.readlines():
            tmp = instr.split(': ')
            layer = SecurityLayer(int(tmp[0]), int(tmp[1]))
            layers.append(layer)
    cost = 0
    delay = 0
    caught = True
    while caught:
        delay += 1
        packet = -1
        caught = False
        print(delay)
        while packet < 100 and caught == False:
            packet += 1
            for layer in layers:
                layer.move()
                if layer.gate == packet and layer.position == 0:
                    caught = True

            if packet == 0:
                for layer in layers:
                    layer.save()
            if caught:
                for layer in layers:
                    layer.reset()
    print(delay)


solve2()


