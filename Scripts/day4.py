def read_passphrases():
    file_name = "Data/day4.txt"
    file = open(file_name, "r")
    passphrases = []
    
    for line in file:
        line = line.strip("\n").split()
        passphrases.append(line)
        
    return passphrases

def valid_passphrases(passphrases):
    count = 0
    
    for phrase in passphrases:
        if len(set(phrase)) == len(phrase):
            count += 1
            
    print(f"Part one: {count}")
    
def valid_anagrams(passphrases):
    count = 0
    
    for phrase in passphrases:
        for i in range(len(phrase)):
            phrase[i] = tuple(sorted(phrase[i]))
            
        if len(set(phrase)) == len(phrase):
            count += 1
            
    print(f"Part two: {count}")
    
if __name__ == "__main__":
    passphrases = read_passphrases()
    valid_passphrases(passphrases)
    valid_anagrams(passphrases)
    