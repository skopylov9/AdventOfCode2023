platform = open('input.txt').read().splitlines()
stonePositions = set([(r, c) for r, line in enumerate(platform) for c, ch in enumerate(line) if ch == 'O'])
rockPositions = [(r, c) for r, line in enumerate(platform) for c, ch in enumerate(line) if ch == '#']
rockPositions.extend([(r, -1) for r in range(len(platform))] + [(r, len(platform[0])) for r in range(len(platform))])
rockPositions.extend([(-1, c) for c in range(len(platform[0]))] + [(len(platform), c) for c in range(len(platform[0]))])
rockPositions = set(rockPositions)

def move(rockPositions, stonePositions, offset):
    newStonePos = set()
    for pos in stonePositions:
        while (pos[0] + offset[0], pos[1] + offset[1]) not in rockPositions and (pos[0] + offset[0], pos[1] + offset[1]) not in newStonePos:
            pos = (pos[0] + offset[0], pos[1] + offset[1])
        while pos in newStonePos:
            pos = (pos[0] - offset[0], pos[1] - offset[1])
        newStonePos.add(pos)
    return newStonePos

def moveCycle(rockPositions, stonePositions):
    for offset in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
        stonePositions = move(rockPositions, stonePositions, offset)
    return stonePositions

stonePositionsPart1 = move(rockPositions, stonePositions, (-1, 0))
print('Part 1: {}'.format(sum([len(platform) - stonePos[0] for stonePos in stonePositionsPart1])))  # 109755

cycle = 0
history = {}
while tuple(stonePositions) not in history:
    history[tuple(stonePositions)] = cycle
    stonePositions = moveCycle(rockPositions, stonePositions)
    cycle += 1

for _ in range((1000000000 - cycle) % (cycle - history[tuple(stonePositions)])):
    stonePositions = moveCycle(rockPositions, stonePositions)

print('Part 2: {}'.format(sum([len(platform) - stonePos[0] for stonePos in stonePositions])))   # 90928
