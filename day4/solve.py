with open("./input.txt") as f:
    grid = f.read().splitlines()

def check(grid, x, y, word='XMAS'):
    m = len(grid)
    n = len(grid[0])

    word_len = len(word)
    radius = word_len - 1

    directions = [(i, j) for i in [-1, 0, 1] for j in [-1, 0, 1]]

    occurences = 0

    for dx, dy in directions:
        if not 0 <= dx * radius + x < n or not 0 <= dy * radius + y < m:
            continue

        for idx, char in enumerate(word):
            if grid[dy * idx + y][dx * idx + x] != char:
                break
        else:
            occurences += 1

    return occurences

def part1(grid):
    total = 0

    m = len(grid)
    n = len(grid[0])

    for x in range(n):
        for y in range(m):
            total += check(grid, x, y)

    return total


def check2(grid, x, y):
    m = len(grid)
    n = len(grid[0])

    if x == 0 or y == 0 or x == n - 1 or y == m - 1:
        return False

    if grid[y][x] != 'A':
        return False


    if { grid[y-1][x-1], grid[y+1][x+1] } != { 'M', 'S' }:
        return False

    if { grid[y-1][x+1], grid[y+1][x-1] } != { 'M', 'S' }:
        return False

    return True

def part2(grid):
    total = 0

    m = len(grid)
    n = len(grid[0])

    for x in range(n):
        for y in range(m):
            if check2(grid, x, y):
                total += 1

    return total

print(part1(grid))
print(part2(grid))
