from functools import reduce
from operator import mul

def calcWaysCount(time, distance):
    count = 0
    for t in range(time):
        if t * (time - t) > distance:
            count += 1
    return count

time, distance = open('input.txt').read().strip().split('\n')

timePart1 = [int(t) for t in time.split(' ')[1:] if t]
distancePart1 = [int(d) for d in distance.split(' ')[1:] if d]

timePart2 = int(time.replace(' ', '').split(':')[1])
distancePart2 = int(distance.replace(' ', '').split(':')[1])

print('Part 1: {}'.format(reduce(mul, [calcWaysCount(timePart1[i], distancePart1[i]) for i in range(len(timePart1))])))  # 2374848
print('Part 2: {}'.format(calcWaysCount(timePart2, distancePart2)))    # 39132886
