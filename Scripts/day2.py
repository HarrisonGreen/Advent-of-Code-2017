def read_spreadsheet():
    file_name = "Data/day2.txt"
    file = open(file_name, "r")
    spreadsheet = []
    
    for line in file:
        line = list(map(int, line.split()))
        spreadsheet.append(line)
        
    return spreadsheet

def checksum(spreadsheet):
    total = 0
    
    for row in spreadsheet:
        total += max(row) - min(row)
        
    print(f"Part one: {total}")
    
def divisible_checksum(spreadsheet):
    total = 0
    
    for row in spreadsheet:
        
        for i in range(len(row)-1):
            for j in range(i+1, len(row)):
                if row[i]%row[j] == 0:
                    total += row[i]//row[j]
                if row[j]%row[i] == 0:
                    total += row[j]//row[i]
                    
    print(f"Part two: {total}")
    
if __name__ == "__main__":
    spreadsheet = read_spreadsheet()
    checksum(spreadsheet)
    divisible_checksum(spreadsheet)
    