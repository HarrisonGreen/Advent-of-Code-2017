import numpy as np

def count_steps(num):
    square = int(np.sqrt(num))
    remainder = num - square**2
    
    step = [(square-1)//2, square//2]
        
    if remainder == 0:
        pass
    elif remainder <= square + 1:
        step[0] += 1
        step[1] = abs(step[1] - remainder + 1)
    else:
        step[1] += square%2
        step[0] = abs(step[0] - remainder + square + 2)
        
    print(f"Part one: {sum(step)}")
    
def stress_test(num):
    dim = 51
    grid = np.zeros([dim, dim], dtype=int)
    pos = [dim//2, dim//2]
    grid[pos[0], pos[1]] = 1
    n = 1
    
    while True:
        n += 1
        square = int(np.sqrt(n))
        remainder = n - square**2
        
        if square%2 == 0:
            if remainder in (0, 1):
                pos[0] -= 1
            elif remainder <= square + 1:
                pos[1] -= 1
            else:
                pos[0] += 1
                
        else:
            if remainder in (0, 1):
                pos[0] += 1
            elif remainder <= square + 1:
                pos[1] += 1
            else:
                pos[0] -= 1
                
        grid[pos[0], pos[1]] = (grid[pos[0]+1, pos[1]] + grid[pos[0]-1, pos[1]] +
                                grid[pos[0], pos[1]+1] + grid[pos[0], pos[1]-1] +
                                grid[pos[0]+1, pos[1]+1] + grid[pos[0]+1, pos[1]-1] +
                                grid[pos[0]-1, pos[1]+1] + grid[pos[0]-1, pos[1]-1])
        
        if grid[pos[0], pos[1]] > num:
            return grid[pos[0], pos[1]]
    
if __name__ == "__main__":
    num = 265149
    count_steps(num)
    print(f"Part two: {stress_test(num)}")
    