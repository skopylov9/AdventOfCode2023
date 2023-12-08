import math
from functools import reduce

lrInstruction, network = open('input.txt').read().split('\n\n')
network = [networkLine.split(' = ') for networkLine in network.splitlines()]
network = {networkLine[0] : (networkLine[1][1:4], networkLine[1][6:9]) for networkLine in network}

def lcm(v1, v2):
    return v1 * v2 // math.gcd(v1, v2)

def stepsForFirstZNode(node):
    steps = 0
    while node[2] != 'Z':
        node = network[node][0 if lrInstruction[steps % len(lrInstruction)] == 'L' else 1]
        steps += 1
    return steps

startNodes = [node for node in network.keys() if node[2] == 'A']

print('Part 1: {}'.format(stepsForFirstZNode('AAA')))   # 20513
print('Part 2: {}'.format(reduce(lcm, [stepsForFirstZNode(node) for node in startNodes])))  # 15995167053923
