plan = [line.split(' ') for line in open('input.txt').read().splitlines()]

def getVLines(plan):
    plan.append(plan[0])

    currPos = (0, 0)
    vlines = []

    for idx, (direction, deep) in enumerate(plan):
        offsetMap = { 'U' : (-1, 0), 'R' : (0, 1), 'D' : (1, 0), 'L' : (0, -1) }
        leftTurn = (plan[idx - 1][0] + direction) in ['UL', 'LD', 'DR', 'RU']
        offset = offsetMap[direction]

        prevDirection = plan[idx - 1][0]
        prevOffset = offsetMap[prevDirection]

        nextPos = (currPos[0] + offset[0] * deep, currPos[1] + offset[1] * deep)
        if direction in 'UD':
            vlines.append(((currPos[0] + (offset[0] if leftTurn else 0), currPos[1]), nextPos))
        elif leftTurn:        
            vlines[-1] = (vlines[-1][0], (vlines[-1][1][0] - prevOffset[0], vlines[-1][1][1]))
        
        currPos = nextPos

    return [tuple(sorted(line)) for line in vlines]

def calc(lines):
    if not lines:
        return 0
    
    lines = sorted(lines, key=lambda line: line[0][1])
    leftLine = lines.pop(0)
    for idx in range(0, len(lines)):
        if lines[idx][1][0] < leftLine[0][0] or lines[idx][0][0] > leftLine[1][0]:
            continue

        crossLine = lines.pop(idx)

        if leftLine[0][0] < crossLine[0][0]:
            lines.append(((leftLine[0][0], leftLine[0][1]), (crossLine[0][0] - 1, leftLine[0][1])))
        elif leftLine[0][0] > crossLine[0][0]:
            lines.append(((crossLine[0][0], crossLine[0][1]), (leftLine[0][0] - 1, crossLine[0][1])))
        
        if leftLine[1][0] + 1 <= crossLine[1][0]:
            lines.append(((leftLine[1][0] + 1, crossLine[0][1]), (crossLine[1][0], crossLine[0][1])))
        elif leftLine[1][0] >= crossLine[1][0] + 1:
            lines.append(((crossLine[1][0] + 1, leftLine[0][1]), (leftLine[1][0], leftLine[0][1])))

        inCrossLine = (max(crossLine[0][0], leftLine[0][0]), min(crossLine[1][0], leftLine[1][0]))
        sq = (crossLine[0][1] - leftLine[0][1] + 1) * (inCrossLine[1] - inCrossLine[0] + 1)
        
        return sq + calc(lines)
    # return calc(lines)

print('Part 1: {}'.format(calc(getVLines([(line[0], int(line[1])) for line in plan]))))                             # 46359
print('Part 2: {}'.format(calc(getVLines([('RDLU'[int(line[2][-2])], int(line[2][2:-2], 16)) for line in plan]))))  # 59574883048274
