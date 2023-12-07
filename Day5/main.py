inputData = open('input.txt').read().split('\n\n')

seeds = [int(seed) for seed in inputData[0].split(': ')[1].split(' ')]
rangedSeeds = [(seeds[i * 2], seeds[i * 2] + seeds[i * 2 + 1]) for i in range(len(seeds) // 2)]

transformMap = dict() 
for inputBlock in inputData[1:]:
    mapDescription = inputBlock.split('\n')
    mapCategory = mapDescription[0].split(' ')[0].split('-to-')

    ranges = []
    for mapRange in mapDescription[1:]:
        dst, src, length = mapRange.split(' ')
        ranges.append((int(dst), int(src), int(length)))
    
    startRange = min([range[1] for range in ranges])
    endRange = max([range[1] + range[2] for range in ranges])
    if startRange != 0:
        ranges = [(0, 0, startRange)] + ranges
    ranges = ranges + [(endRange, endRange, 99999999999)]

    ranges = sorted(ranges, key=lambda range: range[1])
    for i in range(len(ranges) - 1):
        if ranges[i][1] + ranges[i][2] < ranges[i + 1][1]:
            ranges.append((ranges[i][1] + ranges[i][2], ranges[i][1] + ranges[i][2], ranges[i + 1][1] + ranges[i][1] + ranges[i][2]))
    
    transformMap[mapCategory[0]] = (mapCategory[1], ranges)

def getIntersectedRange(ranges, value):
    for range in ranges:
        if range[1] <= value < range[1] + range[2]:
            return range
    return 0

def goThroughTramsform(category, value):
    if category not in transformMap:
        return value
    
    nextCategory, ranges = transformMap[category]
    range = getIntersectedRange(ranges, value)
    return goThroughTramsform(nextCategory, range[0] + (value - range[1]))

def goRangesThroughTramsform(category, ranges):
    if category not in transformMap:
        return ranges
    
    nextCategory, nextRanges = transformMap[category]

    newRanges = []
    for range in ranges:
        start = range[0]
        while True:
            intersectedRange = getIntersectedRange(nextRanges, start)
            
            end = min(intersectedRange[1] + intersectedRange[2], range[1])
            newRanges.append((start + (intersectedRange[0] - intersectedRange[1]), end + (intersectedRange[0] - intersectedRange[1])))
            if end == range[1]:
                break

            start += newRanges[-1][1] - newRanges[-1][0]

    return goRangesThroughTramsform(nextCategory, newRanges)

print('Part 1: {}'.format(min([goThroughTramsform('seed', seed) for seed in seeds])))                   # 261668924
print('Part 2: {}'.format(min([range[0] for range in goRangesThroughTramsform('seed', rangedSeeds)])))  # 24261545
