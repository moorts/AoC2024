import re


with open("./input.txt") as f:
    data = ''.join(f.read().splitlines())


def part1(memory):
    pattern = r"mul\((\d+),(\d+)\)"

    matches = re.findall(pattern, memory)

    total = 0

    for x, y in matches:
        total += int(x) * int(y)

    return total


def part2(memory):
    pattern = r"mul\((\d+),(\d+)\)"

    split_pattern = r"(do\(\))|(don't\(\))"

    sections = re.split(split_pattern, memory)

    active = True

    total = 0

    for section in sections:
        if not section:
            continue
        if section == "do()":
            active = True
        elif section == "don't()":
            active = False

        if active:
            matches = re.findall(pattern, section)

            for x, y in matches:
                total += int(x) * int(y)

    return total


print(part1(data))
print(part2(data))

