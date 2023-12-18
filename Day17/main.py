import heapq

map = [list(map(int, line)) for line in open('input.txt').read().splitlines()]

def getEdges(node, costMap, rangeStart, rangeEnd):
    cost = 0
    edges = []

    for step in range(rangeEnd):
        posOffsets = ((-1, 0), (0, 1), (1, 0), (0, -1))
        nextNode = (node[0] + posOffsets[node[2]][0] * (step + 1), node[1] + posOffsets[node[2]][1] * (step + 1))
        if nextNode[0] not in range(len(map)) or nextNode[1] not in range(len(map[0])):
            continue

        cost += map[nextNode[0]][nextNode[1]]

        if step < rangeStart:
            continue

        edges.append((cost + costMap[node[0]][node[1]][node[2]], (nextNode[0], nextNode[1], (node[2] + 1) % 4)))
        edges.append((cost + costMap[node[0]][node[1]][node[2]], (nextNode[0], nextNode[1], (node[2] + 3) % 4)))

    return edges

def solve(rangeStart, rangeEnd):
    costMap = [[[0 for _ in (0, 1, 2, 3)] for _ in line] for line in map]

    edges = []
    heapq.heapify(edges)
    for node in [(0, 0, 1), (0, 0, 2)]:
        for cost, edge in getEdges(node, costMap, rangeStart, rangeEnd):
            heapq.heappush(edges, (cost, edge))

    while edges:
        cost, nextNode = heapq.heappop(edges)

        if costMap[nextNode[0]][nextNode[1]][nextNode[2]] != 0:
            continue

        costMap[nextNode[0]][nextNode[1]][nextNode[2]] = cost
        for cost, edge in getEdges(nextNode, costMap, rangeStart, rangeEnd):
            heapq.heappush(edges, (cost, edge))
                
    return min(costMap[-1][-1])

print('Part 1: {}'.format(solve(0, 3)))     # 797
print('Part 2: {}'.format(solve(3, 10)))    # 914
