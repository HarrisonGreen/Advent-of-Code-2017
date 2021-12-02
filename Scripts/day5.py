def read_jumps():
    file_name = "Data/day5.txt"
    file = open(file_name, "r")
    jumps = []
    
    for line in file:
        jumps.append(int(line.strip("\n")))
        
    return jumps

def find_exit(jumps):
    pos = 0
    steps = 0
    
    while pos < len(jumps):
        new_pos = pos + jumps[pos]
        jumps[pos] = jumps[pos] + 1
        pos = new_pos
        steps += 1
        
    print(f"Part one: {steps}")
    
def find_new_exit(jumps):
    pos = 0
    steps = 0
    
    while pos < len(jumps):
        new_pos = pos + jumps[pos]
        if jumps[pos] >= 3:
            jumps[pos] = jumps[pos] - 1
        else:
            jumps[pos] = jumps[pos] + 1
        pos = new_pos
        steps += 1
        
    print(f"Part two: {steps}")
    
if __name__ == "__main__":
    jumps = read_jumps()
    find_exit(jumps)
    jumps = read_jumps()
    find_new_exit(jumps)
    