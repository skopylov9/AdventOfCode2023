lines = [ line.split(': ') for line in open('input.txt').read().splitlines() ]
nodes = { line[0] : line[1].split(' ') for line in lines }

for srcNode, dstNodes in list(nodes.items()):
    for dstNode in dstNodes:
        if dstNode not in nodes:
            nodes[dstNode] = []
        if srcNode not in nodes[dstNode]:
            nodes[dstNode].append(srcNode)

def findPath(fromNode, toNode, forbidden):
    visited = set(fromNode)
    queue = [(None, fromNode)]
    def bfs(index):
        _, node = queue[index]
        for dstNode in nodes[node]:
            if (node, dstNode) in forbidden or (dstNode, node) in forbidden:
                continue

            if dstNode not in visited:
                visited.add(dstNode)
                queue.append((index, dstNode))

            if dstNode == toNode:
                return True
        return False
    
    def restorePath():
        path = []
        index = len(queue) - 1
        while queue[index][0] is not None:
            path.append(queue[index][1])
            index = queue[index][0]
        path.append(queue[index][1])
        return list(reversed(path))
    
    index = 0
    while len(queue) > index:
        if bfs(index):
            return restorePath()
        index += 1
    return []

def checkPathAndForbid(fromNode, toNode, forbidden):
    path = findPath(fromNode, toNode, forbidden)
    if not path:
        return False

    for i in range(1, len(path)):
        forbidden.add((path[i - 1], path[i]))
    
    return True

def calcPathCount(fromNode, toNode):
    forbidden = set()
    return sum(1 if checkPathAndForbid(fromNode, toNode, forbidden) else 0 for _ in range(4))

oneSideCount = sum(1 for node in nodes.keys() if calcPathCount(next(iter(nodes)), node) > 3)

print('Part 1:', oneSideCount * (len(nodes) - oneSideCount))    # 798 * 731 = 583338
