from functools import reduce
from operator import mul

inputLines = open('input.txt').read().split('\n')
gameList = [(int(line.split(':')[0].split(' ')[1]), line.split(':')[1].split(';')) for line in inputLines]

# ('red', 'green', 'blue')
borders = (12, 13, 14)

def calcMinCubesEachColor(gameSets):
    return (
        max([int(cubes.split(' ')[1]) for gameSet in gameSets for cubes in gameSet.split(',') if cubes.split(' ')[2] == 'red']),
        max([int(cubes.split(' ')[1]) for gameSet in gameSets for cubes in gameSet.split(',') if cubes.split(' ')[2] == 'green']),
        max([int(cubes.split(' ')[1]) for gameSet in gameSets for cubes in gameSet.split(',') if cubes.split(' ')[2] == 'blue']),
    )

def checkGameSets(gameSets):
    minCubes = calcMinCubesEachColor(gameSets)
    return minCubes[0] <= borders[0] and minCubes[1] <= borders[1] and minCubes[2] <= borders[2]

print('Part 1: {}'.format(sum([gameNum for gameNum, gameSets in gameList if checkGameSets(gameSets)])))     # 2105
print('Part 2: {}'.format(sum([reduce(mul, calcMinCubesEachColor(gameSets)) for _, gameSets in gameList]))) # 72422
