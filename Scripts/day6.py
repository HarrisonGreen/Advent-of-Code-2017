def distribute_blocks(blocks):
    seen = set()
    seen.add(tuple(blocks))
    cycles = 0
    n = len(blocks)

    while True:
        cycles += 1

        for i in range(n):
            if blocks[i] == max(blocks):
                m = blocks[i]
                blocks[i] = 0
                for j in range(m):
                    i = (i + 1)%n
                    blocks[i] += 1
                break

        if tuple(blocks) in seen:
            return cycles, blocks

        seen.add(tuple(blocks))

if __name__ == "__main__":
    blocks = [4,10,4,1,8,4,9,14,5,1,14,15,0,15,3,5]
    cycles, blocks = distribute_blocks(blocks)
    print(f"Part one: {cycles}")
    cycles, blocks = distribute_blocks(blocks)
    print(f"Part two: {cycles}")
    