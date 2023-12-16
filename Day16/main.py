grid = open('input.txt').read().splitlines()

posOffsets = ((-1, 0), (0, 1), (1, 0), (0, -1))

def stepForward(pos):
    return (pos[0] + posOffsets[pos[2]][0], pos[1] + posOffsets[pos[2]][1], pos[2])

def solve(startPos):
    seen = set()
    beamsPos = [startPos]

    while beamsPos:
        beamPos = beamsPos.pop(0)

        if beamPos[0] not in range(len(grid)) or beamPos[1] not in range(len(grid[0])):
            continue

        if beamPos in seen:
            continue
        
        seen.add(beamPos)

        orient = beamPos[2]
        miror = grid[beamPos[0]][beamPos[1]]
        if miror == '.' or (miror == '-' and orient in (1, 3)) or (miror == '|' and orient in (0, 2)):
            beamsPos.append(stepForward((beamPos[0], beamPos[1], orient)))
        elif  (miror == '-' and orient in (0, 2)) or (miror == '|' and orient in (1, 3)):
            beamsPos.append(stepForward((beamPos[0], beamPos[1], (orient + 1) % 4)))
            beamsPos.append(stepForward((beamPos[0], beamPos[1], (orient + 3) % 4)))
        elif  (miror == '/' and orient in (0, 2)) or (miror == '\\' and orient in (1, 3)):
            beamsPos.append(stepForward((beamPos[0], beamPos[1], (orient + 1) % 4)))
        elif  (miror == '/' and orient in (1, 3)) or (miror == '\\' and orient in (0, 2)):
            beamsPos.append(stepForward((beamPos[0], beamPos[1], (orient + 3) % 4)))
    
    return len({(pos[0], pos[1]) for pos in seen})

answerPart1 = solve((0, 0, 1))
answerPart2 = max([max(solve((i, 0, 1)), solve((i, len(grid) - 1, 3)), solve((0, i, 2)), solve((len(grid) - 1, i, 0))) for i in range(len(grid))])

print('Part 1: {}'.format(answerPart1)) # 7307
print('Part 2: {}'.format(answerPart2)) # 7635
