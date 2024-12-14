from parse import compile
from functools import reduce
from operator import mul

tmpl = compile("p={},{} v={},{}")

def parse_robot(robot):
    if res := tmpl.parse(robot):
        return list(map(int, res))

    return []

example = False

if example:
    with open("./example.txt") as f:
        robots = f.read().splitlines()

        robots = [parse_robot(robot) for robot in robots]

    m = 11
    n = 7
else:
    m = 101
    n = 103

    with open("./input.txt") as f:
        robots = f.read().splitlines()

        robots = [parse_robot(robot) for robot in robots]

def solve(robots):
    quadrants = [0 for _ in range(4)]

    for (px, py, vx, vy) in robots:
        x = (px + vx*100) % m
        y = (py + vy*100) % n

        # Compute quadrant
        if x == m // 2 or y == n // 2:
            continue

        quadrant = 2*(x < m // 2) + (y < n // 2)
        quadrants[quadrant] += 1

    return reduce(mul, quadrants)


print(solve(robots))
