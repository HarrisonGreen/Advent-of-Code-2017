from collections import Counter

def read_programs():
    file_name = "Data/day7.txt"
    file = open(file_name, "r")
    programs = {}

    for line in file:
        if "->" not in line:
            line = line.split()
            programs[line[0]] = {"weight": int(line[1][1:-1]), "balanced": []}
        else:
            line = line.strip("\n").split(" -> ")
            line[0] = line[0].split()
            line[1] = line[1].split(", ")
            programs[line[0][0]] = {"weight": int(line[0][1][1:-1]), "balanced": line[1]}

    return programs

def bottom_program(programs):
    all_programs = set()

    for program in programs.keys():
        all_programs.add(program)

    for info in programs.values():
        for program in info["balanced"]:
            all_programs.remove(program)

    print(f"Part one: {list(all_programs)[0]}")

def balance_tower(programs):
    balanced = {}

    for program in programs.keys():
        if len(programs[program]["balanced"]) == 0:
            balanced[program] = True
            continue

        towers = set()

        for base in programs[program]["balanced"]:
            towers.add(get_weight(programs, base))

        if len(towers) == 1:
            balanced[program] = True
        else:
            balanced[program] = False

    for program in programs.keys():
        if not balanced[program]:
            if sum(balanced[tower] for tower in programs[program]["balanced"]) == len(programs[program]["balanced"]):
                unbalanced = program

    weights = []
    for program in programs[unbalanced]["balanced"]:
        weights.append(get_weight(programs, program))

    count = Counter(weights)
    for weight, n in count.items():
        if n == 1:
            odd_one = weight
        else:
            proper_one = weight

    for program in programs[unbalanced]["balanced"]:
        if get_weight(programs, program) == odd_one:
            print(f"Part two: {programs[program]['weight'] + proper_one - odd_one}")

def get_weight(programs, base):
    if len(programs[base]["balanced"]) == 0:
        return programs[base]["weight"]
    else:
        return sum(get_weight(programs, program) for program in programs[base]["balanced"]) + programs[base]["weight"]

if __name__ == "__main__":
    programs = read_programs()
    bottom_program(programs)
    balance_tower(programs)
