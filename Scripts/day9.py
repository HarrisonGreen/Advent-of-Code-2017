def read_stream():
    file_name = "Data/day9.txt"
    file = open(file_name, "r")
    
    for line in file:
        return line.replace("{", "[").replace("}", "]")
    
def remove_garbage(stream):
    
    pos = 0
    while pos < len(stream):
        if stream[pos] != "!":
            pos += 1
        else:
            stream = stream[:pos] + stream[pos+2:]
    
    garbage = 0
    start = 0
    while start < len(stream):
        if stream[start] != "<":
            start += 1
        else:
            for i in range(start+1, len(stream)):
                if stream[i] == ">":
                    end = i
                    break
            stream = stream[:start] + stream[end+1:]
            garbage += end - start - 1
    
    stream = stream.replace("[,", "[").replace(",]", "]")
    stream = eval(stream)
    
    print(f"Part one: {calculate_score(stream, 1)}")
    print(f"Part two: {garbage}")
    
def calculate_score(group, depth):
    return depth + sum(calculate_score(subgroup, depth+1) for subgroup in group)

if __name__ == "__main__":
    stream = read_stream()
    remove_garbage(stream)
    