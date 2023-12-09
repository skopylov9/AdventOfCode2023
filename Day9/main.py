inputLines = open('input.txt').read().splitlines()
inputLinesPart1 = [list(map(int, inputLine.split(' '))) for inputLine in inputLines]
inputLinesPart2 = [list(reversed(list(map(int, inputLine.split(' '))))) for inputLine in inputLines]

def predictNextValue(valueHistory):
    diffHistory = [valueHistory[idx + 1] - valueHistory[idx] for idx in range(len(valueHistory) - 1)]
    return valueHistory[-1] + (0 if not any([v for v in diffHistory]) else predictNextValue(diffHistory))

print('Part 1: {}'.format(sum(map(predictNextValue, inputLinesPart1)))) # 1834108701
print('Part 2: {}'.format(sum(map(predictNextValue, inputLinesPart2)))) # 993s
