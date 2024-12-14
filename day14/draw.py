from PIL import Image
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

def draw(robots, i):
    grid = [['.' for _ in range(m)] for _ in range(n)]
    img = Image.new('RGB', (m, n), 'black')
    pixels = img.load()

    for (px, py, _, _) in robots:
            pixels[px,py] = (255, 255, 255)

    img.save(f"./imgs/robots_{i}.bmp")


def solve(robots):
    for i in range(10000):
        if draw(robots, i):
            break
        new_robots = []
        for (px, py, vx, vy) in robots:
            x = (px + vx) % m
            y = (py + vy) % n

            new_robots.append((x, y, vx, vy))
        robots = new_robots


print(solve(robots))
