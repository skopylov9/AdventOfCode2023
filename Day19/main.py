from functools import reduce
from operator import mul

workflows, parts = open('input.txt').read().split('\n\n')
workflows = [tuple(workflow.split('{')) for workflow in workflows.splitlines()]
workflows = dict([(name, workflow[:-1].split(','))  for name, workflow in workflows])

parts = [tuple([int(val[2:]) for val in part[1:-1].split(',')]) for part in parts.splitlines()]

def doWfRange(wfKey, ranges):
    if wfKey == 'A':
        return reduce(mul, [range[1] - range[0] + 1 for range in ranges])
    elif wfKey == 'R':
        return 0
    
    summ = 0
    workflow = workflows[wfKey]
    for rule in workflow:
        if ':' not in rule:
            continue

        condition, nextWfKey = rule.split(':')
        key, sign, value = condition[0], condition[1], int(condition[2:])
        rangeIdx = 'xmas'.index(key)
        conditionRange = ranges[rangeIdx]
        if sign == '<':
            trueRange = (conditionRange[0], min(value - 1, conditionRange[1]))
            falseRange = (max(conditionRange[0], value), conditionRange[1])
        else:
            trueRange = (max(conditionRange[0], value + 1), conditionRange[1])
            falseRange = (conditionRange[0], min(value, conditionRange[1]))
        
        if trueRange[0] <= trueRange[1]:
            summ += doWfRange(nextWfKey, ranges[:rangeIdx] + (trueRange,) + ranges[rangeIdx + 1:])
        
        if falseRange[0] > falseRange[1]:
            return summ
            
        ranges = ranges[:rangeIdx] + (falseRange,) + ranges[rangeIdx + 1:]
                    
    return summ + doWfRange(workflow[-1], ranges)

part1 = sum([doWfRange('in', ((x, x), (m, m), (a, a), (s, s))) * (x + m + a + s) for x, m, a, s in parts])
part2 = doWfRange('in', ((1, 4000), (1, 4000), (1, 4000), (1, 4000)))

print('Part 1: {}'.format(part1))   # 346230
print('Part 2: {}'.format(part2))   # 124693661917133
