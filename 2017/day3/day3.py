import numpy as np

def solve_day2(target):
    layer = 0
    while (1 + (layer)*2)**2 < target:
        layer += 1
    rem = target - (1+(layer-1)*2)**2
    coords = [layer]*2

    while rem > 0:
        if (coords[1] == -layer):
            coords[1] = layer
        else:
            coords[1] -= 1
            rem -= 1

    #print(coords)
    return coords[0]+abs(coords[1])

def solve_task2(target):
    matrix = np.ndarray((20,20), dtype=int)
    matrix.fill(0)
    start_value = 10
    coords = np.ndarray(2,int)
    coords.fill(start_value)

    layer = 0
    square = 2

    
    matrix[coords[0], coords[1]] = 1


    dirs = [[0,1], [-1,0], [0,-1],[1,0]]
    d = 0
    for i in range(200):
        coords[0] += dirs[d][0]
        coords[1] += dirs[d][1]
        adj_sum = matrix[coords[0]-1, coords[1]-1]
        adj_sum += matrix[coords[0]-1, coords[1]]
        adj_sum += matrix[coords[0]-1, coords[1]+1]
        adj_sum += matrix[coords[0], coords[1]-1]
        adj_sum += matrix[coords[0], coords[1]+1]
        adj_sum += matrix[coords[0]+1, coords[1]-1]
        adj_sum += matrix[coords[0]+1, coords[1]]
        adj_sum += matrix[coords[0]+1, coords[1]+1]
        if (adj_sum > target):
            return adj_sum
        matrix[coords[0], coords[1]] = adj_sum
        square_left = coords.copy()
        square_left[0] += dirs[(d+1)%4][0]
        square_left[1] += dirs[(d+1)%4][1]
        if (matrix[square_left[0], square_left[1]] == 0):
            d = (d+1)%4
        square += 1
    return 0
        



print(solve_day2(325489))
print(solve_task2(325489))


