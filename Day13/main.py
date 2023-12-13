grids = [grid.splitlines() for grid in open('input.txt').read().split('\n\n')]

gridsH = [[set([idx for idx, ch in enumerate(line) if ch == '#']) for line in grid] for grid in grids]
gridsV = [[set([idx for idx, ch in enumerate(line) if ch == '#']) for line in zip(*grid)] for grid in grids]

def findReflection(grid, allowedErrors):
    for row in range(0, len(grid) - 1):
        errors = 0
        for offset in range(min(row + 1, len(grid) - row - 1)):
            errors += len(grid[row - offset] - grid[row + offset + 1])
            errors += len(grid[row + offset + 1]- grid[row - offset])

            if errors > allowedErrors:
                break
        else:
            if errors == allowedErrors:
                return row + 1
    return 0

def solve(allowedErrors):
    hReflectionSum = sum([findReflection(grid, allowedErrors) for grid in gridsH])
    vReflectionSum = sum([findReflection(grid, allowedErrors) for grid in gridsV])
    return 100 * hReflectionSum + vReflectionSum

print('Part 1: {}'.format(solve(0)))    # 30575
print('Part 2: {}'.format(solve(1)))    # 37478
