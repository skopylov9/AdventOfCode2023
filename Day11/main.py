grid = open('input.txt').read().splitlines()

galaxies = [(r, c) for r, line in enumerate(grid) for c, ch in enumerate(line) if ch == '#']
rowExpands = [r for r, line in enumerate(grid) if '#' not in line]
columpExpands = [c for c, line in enumerate(zip(*grid)) if '#' not in line]

def expand(galaxies, rowExpands, columpExpands, value):
    for row in reversed(rowExpands):
        galaxies = [(r, c) if r < row else (r + value, c) for r, c in galaxies]

    for column in reversed(columpExpands):
        galaxies = [(r, c) if c < column else (r, c + value) for r, c in galaxies]
    
    return galaxies

def calcDistanceSum(galaxies):
    return sum([abs(g1[0] - g2[0]) + abs(g1[1] - g2[1]) for g1 in galaxies for g2 in galaxies]) // 2

print('Part 1: {}'.format(calcDistanceSum(expand(galaxies, rowExpands, columpExpands, 1))))         # 10292708
print('Part 2: {}'.format(calcDistanceSum(expand(galaxies, rowExpands, columpExpands, 999999))))    # 790194712336