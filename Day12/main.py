from functools import lru_cache

records = [record.split(' ') for record in open('input.txt').read().splitlines()]
records1 = [(record[0], tuple(map(int, record[1].split(',')))) for record in records]
records2 = [('?'.join([record[0]] * 5), tuple(map(int, record[1].split(','))) * 5) for record in records]

def fit(mask, template, last = False):
    startIdx = len(mask) - template - 1 + (1 if last else 0)
    cuttedMaskOut = mask[:startIdx] + mask[startIdx + template:]
    cuttedMaskIn = mask[startIdx : startIdx + template]
    return '.' not in cuttedMaskIn and '#' not in cuttedMaskOut

@lru_cache(maxsize=None)
def solveRecord(mask, temlates):
    if not temlates:
        return 1 if '#' not in mask else 0

    templateFixed = temlates[0] + (0 if (len(temlates) == 1) else 1)
    maskPairs = [(mask[: i + templateFixed], mask[i + templateFixed :]) for i in range(0, len(mask) - templateFixed + 1)]
    return sum([solveRecord(maskPair[1], temlates[1:]) if fit(maskPair[0], temlates[0], len(temlates) == 1) else 0 for maskPair in maskPairs])

print('Part 1: {}'.format(sum([solveRecord(record[0], record[1]) for record in records1])))  # 7251
print('Part 2: {}'.format(sum([solveRecord(record[0], record[1]) for record in records2])))  # 2128386729962