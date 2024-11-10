mapLen = 9
repeats = 4
matrix = [['.' for _ in range(mapLen * (repeats * 2 + 1))] for _ in range(mapLen * (repeats * 2 + 1))]
start = (repeats * mapLen + mapLen // 2, repeats * mapLen + mapLen // 2)
dist = repeats * mapLen + mapLen // 2

matrix[start[0]][start[1]] = 'S'

def printRaw(r, m):
    res = []
    for b in range(repeats * 2 + 1):
        res.append(''.join(m[r][b * mapLen : (b + 1) * mapLen]))
    
    print(' '.join(res))

def printMatrix(m):
    for r in range(mapLen * (repeats * 2 + 1)):
        if mapLen and not r % mapLen:
            print()
        printRaw(r, m)

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        cDist = abs(start[0] - i) + abs(start[1] - j)
        if (cDist < dist and cDist % 2):
            matrix[i][j] = '*'

printMatrix(matrix)