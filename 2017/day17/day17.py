import numpy as np
from numba import jit


@jit
def part_a(step_size, final_size, pos):
    current_pos = 0
    final = 0
    for i in range(1, final_size):
        current_pos = ((current_pos + step_size) % i) + 1
        if current_pos == pos:
            final = i

    return final


def main():
    inp = 345
    final_size = 50000000
    print(part_a(inp, final_size, 1))


if __name__ == "__main__":
    main()
