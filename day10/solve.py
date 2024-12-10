from functools import reduce

with open("./input.txt") as f:
    grid = f.read().splitlines()
    grid = [[int(x) for x in row] for row in grid]

def part1(grid):
    cache = dict()

    n = len(grid)
    m = len(grid[0])

    heights = [[] for _ in range(10)]

    for y in range(n):
        for x in range(m):
            heights[grid[y][x]].append((x, y))

    for (x, y) in heights[9]:
        cache[(x, y)] = { (x, y) }

    for height in range(8, -1, -1):
        for (x, y) in heights[height]:
            reachable = set()
            for nx, ny in [(x + dx, y + dy) for dx in [-1, 0, 1] for dy in [-1, 0, 1] if abs(dx + dy) == 1]:
                if 0 <= nx < m and 0 <= ny < n:
                    if grid[ny][nx] == height + 1:
                        reachable |= cache[(nx, ny)]
            cache[(x, y)] = reachable

    total = 0
    for (x, y) in heights[0]:
        total += len(cache[(x, y)])

    return total

def part2(grid):
    cache = dict()

    n = len(grid)
    m = len(grid[0])

    heights = [[] for _ in range(10)]

    for y in range(n):
        for x in range(m):
            heights[grid[y][x]].append((x, y))

    for (x, y) in heights[9]:
        cache[(x, y)] = 1

    for height in range(8, -1, -1):
        for (x, y) in heights[height]:
            good_trails = 0
            for nx, ny in [(x + dx, y + dy) for dx in [-1, 0, 1] for dy in [-1, 0, 1] if abs(dx + dy) == 1]:
                if 0 <= nx < m and 0 <= ny < n:
                    if grid[ny][nx] == height + 1:
                        good_trails += cache[(nx, ny)]
            cache[(x, y)] = good_trails

    
    return sum([cache[(x, y)] for (x, y) in heights[0]])



print(part1(grid))
print(part2(grid)) #?
