with open("./input.txt") as f:
    lines = f.read().splitlines()

    rows = [line.split(": ") for line in lines]

    rows = [(int(test_value), list(map(int, inputs.split(" ")))) for (test_value, inputs) in rows]

def check(test_value, inputs, prev=0, part2=False):
    if len(inputs) == 0:
        return test_value == prev

    if prev > test_value:
        return False

    val1 = prev + inputs[0]
    val2 = prev * inputs[0]
    val3 = int(str(prev) + str(inputs[0]))

    return check(test_value, inputs[1:], val1, part2) or check(test_value, inputs[1:], val2, part2) or (part2 and check(test_value, inputs[1:], val3, part2))


def part1(rows):
    return sum([test_value for test_value, inputs in rows if check(test_value, inputs)])

def part2(rows):
    return sum([test_value for test_value, inputs in rows if check(test_value, inputs, part2=True)])



print(part1(rows))
print(part2(rows))
