def read_captcha():
    file_name = "Data/day1.txt"
    file = open(file_name, "r")
    
    for line in file:
        return line.strip("\n")
        
def solve_captcha(captcha):
    total = 0
    
    for i in range(len(captcha)):
        if captcha[i] == captcha[(i+1)%len(captcha)]:
            total += int(captcha[i])
            
    print(f"Part one: {total}")
    
def solve_halfway_captcha(captcha):
    total = 0
    
    for i in range(len(captcha)):
        if captcha[i] == captcha[(i+len(captcha)//2)%len(captcha)]:
            total += int(captcha[i])
            
    print(f"Part two: {total}")
    
if __name__ == "__main__":
    captcha = read_captcha()
    solve_captcha(captcha)
    solve_halfway_captcha(captcha)
    