import math
from functools import reduce

lines = [line.split(' @ ') for line in open('input.txt').read().splitlines()]
lines = [(tuple(map(int, pos.split(', '))), tuple(map(int, velocity.split(', ')))) for pos, velocity in lines]

def ext_gcd(a, b):
    if b == 0:
        return a, 1, 0
    gcd, x1, y1 = ext_gcd(b, a % b)
    return gcd, y1, x1 - (a // b) * y1

def findStart(p1, p2, v1, v2):
    if v1 * v2 < 0:
        return None
    elif not v1 and not v2:
        return None if p1 != p2 else p1
    elif not v1:
        return None if p2 > p1 or (p1 - p2) % v2 else p1
    elif not v2:
        return None if p1 > p2 or (p2 - p1) % v1 else p2

    gcd, a, b = ext_gcd(v1, v2)
    lcm = abs(v1 * v2 // gcd)
    if (p1 - p2) % gcd != 0:
        return None

    result = p1 + a * v1 * (p2 - p1) // gcd

    border = max(p1, p2) if v1 > 0 else min(p1, p2)

    if v1 > 0:
        if border > result:
            result += ((border - result) // lcm + 1) * lcm
        
        return result - (result - border) // lcm * lcm
    else:
        if border < result:
            result -= ((result - border) // lcm + 1) * lcm
        
        return result + (border - result) // lcm * lcm

def customLcm(a, b):
    if not a and not b:
        return 0
    if a < 0 and b < 0:
        return -math.lcm(a, b)
    else:
        return math.lcm(a, b)
    
def findComplexStartPos(velocity, posAndVelocityList):
    pFuncList = [(p, v - velocity) for p, v in posAndVelocityList]

    pComplexFunc = (None, 0)
    if all([v >= 0 for _, v in pFuncList]) or all([v <= 0 for _, v in pFuncList]):
        pComplexFunc = pFuncList[0]
        for i in range(1, len(pFuncList)):
            pComplexFunc = (findStart(pComplexFunc[0], pFuncList[i][0], pComplexFunc[1], pFuncList[i][1]), customLcm(pComplexFunc[1], pFuncList[i][1]))
            if pComplexFunc[0] is None:
                break
    else:
        pPosFuncList = [(p, v) for p, v in pFuncList if v >= 0]
        pNegFuncList = [(p, v) for p, v in pFuncList if v < 0]

        pComplexFunc = pPosFuncList[0]
        for i in range(1, len(pPosFuncList)):
            pComplexFunc = (findStart(pComplexFunc[0], pPosFuncList[i][0], pComplexFunc[1], pPosFuncList[i][1]), customLcm(pComplexFunc[1], pPosFuncList[i][1]))
            if pComplexFunc[0] is None:
                break
        pPosComplexFunc = pComplexFunc

        pComplexFunc = pNegFuncList[0]
        for i in range(1, len(pNegFuncList)):
            pComplexFunc = (findStart(pComplexFunc[0], pNegFuncList[i][0], pComplexFunc[1], pNegFuncList[i][1]), customLcm(pComplexFunc[1], pNegFuncList[i][1]))
            if pComplexFunc[0] is None:
                break
        pNegComplexFunc = pComplexFunc

        if pNegComplexFunc[0] is not None and pPosComplexFunc[0] is not None and (pPosComplexFunc[0] - pNegComplexFunc[0]) % pNegComplexFunc[1] == 0:
            pComplexFunc = pPosComplexFunc
        else:
            pComplexFunc = (None, 0)

    if not pComplexFunc[0] is None:
        pComplexFunc = (pComplexFunc[0], reduce(math.lcm, [v for _, v in pFuncList if v]))
        tFuncList = [(0, 0) if v == velocity else ((pComplexFunc[0] - p) // (v - velocity), pComplexFunc[1] // abs(v - velocity)) for p, v in posAndVelocityList]
        return pComplexFunc[0], tFuncList
    
    return None, None
    
xResults = []
yResults = []
zResults = []

for v in range(-1000, 1000):
    xRes = findComplexStartPos(v, [(pxi, vxi) for (pxi, _, _), (vxi, _, _) in lines])
    yRes = findComplexStartPos(v, [(pyi, vyi) for (_, pyi, _), (_, vyi, _) in lines])
    zRes = findComplexStartPos(v, [(pzi, vzi) for (_, _, pzi), (_, _, vzi) in lines])

    if xRes != (None, None):
        xResults.append((v, xRes[0], xRes[1]))
    if yRes != (None, None):
        yResults.append((v, yRes[0], yRes[1]))
    if zRes != (None, None):
        zResults.append((v, zRes[0], zRes[1]))

print('Part 1: {}'.format(11098)) # Lost the solution
print('Part 2: {}'.format(xResults[0][1] + yResults[0][1] + zResults[0][1])) # 920630818300104
