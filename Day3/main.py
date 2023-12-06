import re

inputLines = open('input.txt').read().split('\n')

def checkIsSymbol(ch):
    return ch not in '0123456789.'

def getBorder(i, start, end):
    border = [(i, start - 1), (i + 1, start - 1), (i - 1, start - 1)]
    border += [(i, end), (i + 1, end), (i - 1, end)]
    border += [(i - 1, j) for j in range(start, end)]
    border += [(i + 1, j) for j in range(start, end)]
    return border

def checkAdjacent(i, start, end):
    for border in getBorder(i, start, end):
        if border in symbolsPos:
            return True
    return False

def checkAsterixAdjacent(i, start, end, value):
    for border in getBorder(i, start, end):
        if border in asterixNeighbourMap:
            asterixNeighbourMap[border].append(value)

symbolsPos = set([(i, j) for i, line in enumerate(inputLines) for j, ch in enumerate(line) if checkIsSymbol(ch)])
asterixNeighbourMap = dict([((i, j), []) for i, line in enumerate(inputLines) for j, ch in enumerate(line) if ch == '*'])

nums = []
for i, line in enumerate(inputLines):
    for match in re.finditer('[0-9]+', line):        
        if checkAdjacent(i, match.start(), match.end()):
            nums.append(int(match.group()))
            checkAsterixAdjacent(i, match.start(), match.end(), int(match.group()))

print('Part 1: {}'.format(sum(nums)))   # 544664
print('Part 2: {}'.format(sum([neighbourList[0] * neighbourList[1] for neighbourList in asterixNeighbourMap.values() if len(neighbourList) == 2]))) # 84495585
