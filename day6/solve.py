from collections import defaultdict
import copy

with open("./input.txt") as f:
    data = f.read().splitlines()

    grid = [[c for c in row] for row in data]

def locate_guard(grid):
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if grid[y][x] in ["<", ">", "^", "v"]:
                return (x, y)

def find_loop(grid):
    gx, gy = locate_guard(grid)
    dx, dy = 0, -1

    n = len(grid)
    m = len(grid[0])

    seen = defaultdict(set)

    x, y = gx, gy
    seen[(x, y)].add((dx, dy))

    while True:
        next_x, next_y = x + dx, y + dy

        if next_x < 0 or next_x  >= m or next_y < 0 or next_y >= n:
            # Guard left the grid
            break

        while grid[y + dy][x + dx] == '#':
            dx, dy = -dy, dx
            # seen[(x,y)].add((dx, dy))

        next_x, next_y = x + dx, y + dy

        if (dx, dy) in seen[(next_x, next_y)]:
            # Guard was here in the same direction already -> loop
            return True

        x, y = next_x, next_y
        seen[(x,y)].add((dx, dy))


    return False

def traverse(grid):
    gx, gy = locate_guard(grid)

    n = len(grid)
    m = len(grid[0])

    dx, dy = 0, -1

    seen = defaultdict(set)

    x, y = gx, gy
    seen[(x, y)].add((dx, dy))

    while True:
        next_x, next_y = x + dx, y + dy

        if next_x < 0 or next_x  >= m or next_y < 0 or next_y >= n:
            # Guard left the grid
            break

        while grid[y + dy][x + dx] == '#':
            dx, dy = -dy, dx
            
        next_x, next_y = x + dx, y + dy

        if (dx, dy) in seen[(next_x, next_y)]:
            # Guard was here in the same direction already -> loop
            break

        x, y = next_x, next_y
        seen[(x,y)].add((dx, dy))

    return seen

def part1(grid):
    return len(traverse(grid))

def part2(grid):
    points = traverse(grid)

    total = 0

    for x, y in points:
        if grid[y][x] == '^':
            continue
        grid[y][x] = '#'
        if find_loop(grid):
            total += 1
        grid[y][x] = '.'

    return total

print(part1(grid))
print(part2(grid))
