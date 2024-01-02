field = [list(line) for line in open('input.txt').read().splitlines()]
startPos = (0, field[0].index('.'))
endPos = (len(field) - 1, field[-1].index('.'))
nodes = [startPos, endPos]
for r in range(1, len(field) - 1):
    for c in range(1, len(field[0]) - 1):
        if field[r][c] == '#':
            continue
        if sum([1 if field[r + dx][c + dy] != '#' else 0 for dx, dy in ((0, 1), (0, -1), (1, 0), (-1, 0))]) > 2:
            nodes.append((r, c))

def getMovesPart1(field, currentPos):
    possibleMoves = {
        '.' : ((0, 1), (0, -1), (1, 0), (-1, 0)),
        '^' : ((-1, 0), ),
        '>' : ((0, 1), ),
        'v' : ((1, 0), ),
        '<' : ((0, -1), ),
    }
    return possibleMoves[field[currentPos[0]][currentPos[1]]]

def getMovesPart2(field, currentPos):
    return ((0, 1), (0, -1), (1, 0), (-1, 0))

def getNextPositions(field, currentPos, getMoves, prevPos = (-1, -1)):
    nextPositions = []
    for dx, dy in getMoves(field, currentPos):
        nextPos = (currentPos[0] + dx, currentPos[1] + dy)
        if nextPos[0] in range(len(field)) and nextPos[1] in range(len(field[0])):
            if nextPos != prevPos and field[nextPos[0]][nextPos[1]] != '#':
                nextPositions.append(nextPos)
    return nextPositions

def makeGraph(field, nodes, getMoves):
    graph = dict()
    for node in nodes:
        graph[node] = []

        nextPositions = getNextPositions(field, node, getMoves)
        for nextPos in nextPositions:
            prevPos = node
            distance = 1
            while len(getNextPositions(field, nextPos, getMoves, prevPos)) == 1:
                prevPos, nextPos = nextPos, getNextPositions(field, nextPos, getMoves, prevPos)[0]
                distance += 1
            
            if nextPos in nodes:
                graph[node].append((nextPos, distance))
    
    return graph

def dfs(graph, startNode, endNode, allowedNodes):
    if startNode == endNode:
        return 0
    allowedNodes.remove(startNode)
    result = -1000000
    for node, distance in graph[startNode]:
        if node not in allowedNodes:
            continue
        result = max(result, dfs(graph, node, endNode, allowedNodes) + distance)
    allowedNodes.add(startNode)
    return result

print('Part 1: {}'.format(dfs(makeGraph(field, nodes, getMovesPart1), startPos, endPos, set(nodes))))   # 2214
print('Part 2: {}'.format(dfs(makeGraph(field, nodes, getMovesPart2), startPos, endPos, set(nodes))))   # 6594
