from functools import cache

with open("./input.txt") as f:
    stones = [int(stone) for stone in f.read().strip().split(" ")]

def rule1(stone):
    if stone == 0:
        return [1]

    return None

def rule2(stone):
    stone_str = str(stone)
    l = len(stone_str)

    if l % 2 == 0:
        return [int(stone_str[:l // 2]), int(stone_str[l // 2:])]

    return None

def rule3(stone):
    return [stone * 2024]


rules = [
    rule1,
    rule2,
    rule3
]

def blink(stones):
    new_stones = []
    for stone in stones:
        for rule in rules:
            if new := rule(stone):
                new_stones += new
                break

    return new_stones

@cache
def recurse(stone, blink=0, num_blinks=75):
    if blink == num_blinks:
        return 1
    for rule in rules:
        if new := rule(stone):
            return sum([recurse(stone, blink=blink+1, num_blinks=num_blinks) for stone in new])

    return 0

def part1(stones):
    return sum([recurse(stone, num_blinks=25) for stone in stones])

def part2(stones):
    return sum([recurse(stone) for stone in stones])

print(part1(stones))
print(part2(stones))


