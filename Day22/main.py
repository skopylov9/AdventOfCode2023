bricks = [line.split('~') for line in open('input.txt').read().splitlines()]
bricks = [(tuple(map(int, brick[0].split(','))), tuple(map(int, brick[1].split(',')))) for brick in bricks]
bricks = [(brick[1], brick[0]) if brick[0] > brick[1] else (brick[0], brick[1]) for brick in bricks]
bricks = sorted(bricks, key=lambda brick: brick[0][2])

field = [[[0 for _ in range(321)] for _ in range(10)] for _ in range(10)]
for idx, brick in enumerate(bricks):
    for z in range(brick[0][2], -1, -1):
        fit = True
        for x in range(brick[0][0], brick[1][0] + 1):
            for y in range(brick[0][1], brick[1][1] + 1):
                if field[x][y][z] != 0:
                    fit = False
                    break
        if not fit or not z:
            for x in range(brick[0][0], brick[1][0] + 1):
                for y in range(brick[0][1], brick[1][1] + 1):
                    for zOffset in range(brick[1][2] - brick[0][2] + 1):
                        field[x][y][z + zOffset + (1 if fit or z else 0)] = idx + 1
            break

bricksSupports = [set() for _ in range(len(bricks))]
bricksSupportedBy = [set() for _ in range(len(bricks))]

for z in range(len(field[0][0]) - 1):
    for x in range(len(field)):
        for y in range(len(field[0])):
            if field[x][y][z] != 0:
                if field[x][y][z + 1] != 0 and field[x][y][z + 1] != field[x][y][z]:
                    bricksSupportedBy[field[x][y][z + 1] - 1].add(field[x][y][z] - 1)
                    bricksSupports[field[x][y][z] - 1].add(field[x][y][z + 1] - 1)

part1 = 0
part2 = 0
for i in range(len(bricks)):
    if not len(bricksSupports[i]) or all([len(bricksSupportedBy[brickIdx]) > 1 for brickIdx in bricksSupports[i]]):
        part1 += 1
        
    seen = set([i])
    toCheckQueue = list(bricksSupports[i])
    while toCheckQueue:
        toCheckBrickIdx = toCheckQueue.pop(0)
        if all([brickIdx in seen for brickIdx in bricksSupportedBy[toCheckBrickIdx]]):
            seen.add(toCheckBrickIdx)
            toCheckQueue.extend(bricksSupports[toCheckBrickIdx])
    part2 += len(seen) - 1

print('Part 1: {}'.format(part1))   # 398
print('Part 2: {}'.format(part2))   # 70727