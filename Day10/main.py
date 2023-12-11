map = open('input.txt').read().splitlines()

for idx, line in enumerate(map):
    if 'S' in line:
        startPos = (idx, line.index('S'))
        break

posValueTransitions = {
    '|' : (1, 0, 1, 0),
    '-' : (0, 1, 0, 1),
    'L' : (1, 1, 0, 0),
    'J' : (1, 0, 0, 1),
    '7' : (0, 0, 1, 1),
    'F' : (0, 1, 1, 0),
    'S' : (1, 1, 1, 1),
    '.' : (0, 0, 0, 0),
}

orientTransitions = {
    0 : { '|' : 0, '7' : 3, 'F' : 1 },
    1 : { '-' : 1, 'J' : 0, '7' : 2 },
    2 : { '|' : 2, 'L' : 1, 'J' : 3 },
    3 : { '-' : 3, 'L' : 0, 'F' : 2 },
}

fillTransitions = {
    ('|', 0) : ((0, 1),),
    ('|', 2) : ((0, -1),),
    ('-', 1) : ((1, 0),),
    ('-', 3) : ((-1, 0),),
    ('L', 1) : ((0, -1), (1, 0)),
    ('J', 0) : ((0, 1), (1, 0)),
    ('7', 3) : ((0, 1), (-1, 0)),
    ('F', 2) : ((0, -1), (-1, 0)),
}

path = []
otherMap = [[0 for _ in range(len(map[0]))] for _ in range(len(map))]

def getNextPos(pos):
    for dx, dy, con in ((-1, 0, 0), (0, 1, 1), (1, 0, 2), (0, -1, 3)):
        nextPos = (pos[0] + dx, pos[1] + dy)
        if nextPos[0] not in range(len(map)) or nextPos[1] not in range(len(map[0])):
            continue

        if posValueTransitions[map[pos[0]][pos[1]]][con]:
            if posValueTransitions[map[nextPos[0]][nextPos[1]]][(con + 2) % 4]:
                if otherMap[nextPos[0]][nextPos[1]] == 0:
                    return nextPos

lastPos = startPos
while lastPos:
    path.append(lastPos)
    otherMap[lastPos[0]][lastPos[1]] = 1
    lastPos = getNextPos(lastPos)

def fillInner(pos):
    fillQueue = [pos]
    while fillQueue:
        pos, *fillQueue = fillQueue
        
        if pos[0] not in range(len(otherMap)) or pos[1] not in range(len(otherMap[0])):
            continue

        if otherMap[pos[0]][pos[1]] == 0:
            otherMap[pos[0]][pos[1]] = 'X'

            for dx, dy in ((0, 1), (0, -1), (1, 0), (-1, 0)):
                if (pos[0] + dx, pos[1] + dy) not in fillQueue:
                    fillQueue.append((pos[0] + dx, pos[1] + dy))

orient = [(-1, 0), (0, 1) , (1, 0), (0, 1)].index((path[1][0] - path[0][0], path[1][1] - path[0][1]))
for pos in path[1:]:
    posVal = map[pos[0]][pos[1]]
    orient = orientTransitions[orient][posVal]

    if (posVal, orient) in fillTransitions:
        for dx, dy in fillTransitions[(posVal, orient)]:
            fillInner((pos[0] + dx, pos[1] + dy))

innerOrOuterBlockSize = sum([1 if ch == 'X' else 0 for line in otherMap for ch in line])
print('Part 1: {}'.format(len(path) // 2 + len(path) % 2))                                                          # 6968
print('Part 2: {} or {}'.format(innerOrOuterBlockSize, len(map) * len(map[0]) - len(path) - innerOrOuterBlockSize)) # 413
