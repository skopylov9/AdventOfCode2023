map = open('input.txt').read().splitlines()

mapLen = len(map)
stepsPart1 = 64
stepsPart2 = 26501365
repeats = 2
stepsPart2Ahead = stepsPart2 % mapLen

startPos = (mapLen // 2, mapLen // 2)
map[startPos[0]] = map[startPos[0]][:startPos[1]] + '.' + map[startPos[0]][startPos[1] + 1:]
for i in range(len(map)):
    map[i] *= repeats * 2 + 1
map *= repeats * 2 + 1
startPos = (startPos[0] + mapLen * repeats, startPos[1] + mapLen * repeats)

def calcVisited(map, steps, startPos):
    posQueue = [startPos]
    visited = set()

    for index in range(steps):
        newPosQueue = set()
        for pos in posQueue:
            for dx, dy in ((0, 1), (0, -1), (1, 0), (-1, 0)):
                nextPos = (pos[0] + dx, pos[1] + dy)
                if map[nextPos[0]][nextPos[1]] != '#' and nextPos not in newPosQueue:
                    newPosQueue.add(nextPos)

        posQueue = []
        if (index + 1) % 2 == steps % 2:
            for newPos in newPosQueue:
                if newPos not in visited:
                    visited.add(newPos)
                    posQueue.append(newPos)
        else:
            posQueue = list(newPosQueue)
    
    return visited

# (fullMapEven + fullMapOdd) * pow(repeats, 2) + (fourSides1 + fourSides2 - 2 * fullMapOdd) * repeats + (fourPeaks - fourSides2 + fullMapOdd)

def calcVisitedCountOnInf(steps, mapLen, fullMapEven, fullMapOdd, fourSides1, fourSides2, fourPeaks):
    repeats = steps // mapLen
    result = 0
    result += repeats * repeats * fullMapEven
    result += (repeats - 1) * (repeats - 1) * fullMapOdd
    result += repeats * fourSides1
    result += (repeats - 1) * fourSides2
    result += fourPeaks
    return result

visitedPart2 = calcVisited(map, mapLen * repeats + stepsPart2Ahead, startPos)

topAndBottomPeak = sum([1 if (i < mapLen or i >= mapLen * repeats * 2) and j in range(mapLen * repeats, mapLen * repeats + mapLen) else 0 for i, j in visitedPart2])
leftAndRightPeak = sum([1 if i in range(mapLen * repeats, mapLen * repeats + mapLen) and (j < mapLen or j >= mapLen * repeats * 2) else 0 for i, j in visitedPart2])
fourPeaks = topAndBottomPeak + leftAndRightPeak

fullMapEven = sum([1 if i in range(mapLen, 2 * mapLen) and j in range(mapLen * repeats, mapLen * repeats + mapLen) else 0 for i, j in visitedPart2])
fullMapOdd = sum([1 if i in range(mapLen * repeats, mapLen * repeats + mapLen) and j in range(mapLen * repeats, mapLen * repeats + mapLen) else 0 for i, j in visitedPart2])

fourSides1 = sum([1 if i < mapLen or i >= mapLen * repeats * 2 else 0 for i, j in visitedPart2]) - topAndBottomPeak

fourSides2 = len(visitedPart2) - calcVisitedCountOnInf(mapLen * repeats + stepsPart2Ahead, mapLen, fullMapEven, fullMapOdd, fourSides1, 0, fourPeaks)
fourSides2 //= repeats - 1

part1 = len(calcVisited(map, stepsPart1, startPos))
part2 = calcVisitedCountOnInf(stepsPart2, mapLen, fullMapEven, fullMapOdd, fourSides1, fourSides2, fourPeaks)

print('Part 1: {}'.format(part1))   # 3773
print('Part 2: {}'.format(part2))   # 625628021226274
