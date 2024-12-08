from itertools import combinations
from math import gcd

with open("input.txt") as f:
    grid = f.read().splitlines()

def get_antennas(grid):
    antennas = dict()
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if grid[y][x] == '.':
                continue
            if grid[y][x] in antennas:
                antennas[grid[y][x]].add((x, y))
            else:
                antennas[grid[y][x]] = { (x, y) }

    return antennas


def part1(grid):
    m = len(grid)
    n = len(grid[0])
    antennas = get_antennas(grid)

    antinodes = set()

    for locations in antennas.values():
        for (x1, y1), (x2, y2) in combinations(locations, 2):
            antinode1 = (x2 + 2*x1 - 2*x2, y2 + 2*y1 - 2*y2)
            antinode2 = (x1 + 2*x2 - 2*x1, y1 + 2*y2 - 2*y1)

            if 0 <= antinode1[0] < m and 0 <= antinode1[1] < n:
                antinodes.add(antinode1)

            if 0 <= antinode2[0] < m and 0 <= antinode2[1] < n:
                antinodes.add(antinode2)

    return len(antinodes)



def part2(grid):
    m = len(grid)
    n = len(grid[0])
    antennas = get_antennas(grid)

    antinodes = set()

    for locations in antennas.values():
        for (x1, y1), (x2, y2) in combinations(locations, 2):
            dx, dy = (x1 - x2, y1 - y2)

            # Simplify the fraction
            q = gcd(dx, dy)

            dx, dy = dx // q, dy // q

            x, y = x1, y1

            while 0 <= x < m and 0 <= y < n:
                antinodes.add((x, y))
                x += dx
                y += dy

            x, y = x1, y1

            while 0 <= x < m and 0 <= y < n:
                antinodes.add((x, y))
                x -= dx
                y -= dy

    return len(antinodes)


print(part1(grid))
print(part2(grid))
