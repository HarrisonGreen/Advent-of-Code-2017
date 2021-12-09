def read_instructions():
    file_name = "Data/day8.txt"
    file = open(file_name, "r")
    instructions = []
    
    for line in file:
        line = line.split()
        line = [line[0], line[1], int(line[2]), line[4], line[5], int(line[6])]
        instructions.append(line)
        
    return instructions

def find_register_values(instructions):
    registers = {}
    maximum = 0
    
    for instr in instructions:
        registers[instr[0]] = registers.get(instr[0], 0)
        registers[instr[3]] = registers.get(instr[3], 0)
        
        if eval(f"{registers[instr[3]]} {instr[4]} {instr[5]}"):
            if instr[1] == "dec":
                instr[2] *= -1
            registers[instr[0]] += instr[2]
            maximum = max(maximum, registers[instr[0]])
            
    print(f"Part one: {max(registers.values())}")
    print(f"Part two: {maximum}")
        
if __name__ == "__main__":
    instructions = read_instructions()
    find_register_values(instructions)
    