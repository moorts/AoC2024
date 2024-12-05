with open("./input.txt") as f:
    data = f.read()

instructions, orderings = data.split("\n\n")


instructions = [line.split("|") for line in instructions.splitlines()]

lookup = dict()

for x, y in instructions:
    if x in lookup:
        lookup[x].add(y)
    else:
        lookup[x] = set([y])

    
orderings = [order.split(",") for order in orderings.splitlines()]

def check_ordering(lookup, order):
    prev_pages = set()
    for page in order:
        if page in lookup and len(prev_pages & lookup[page]) > 0:
            return False

        prev_pages.add(page)
    return True



def part1(lookup, orders):
    total = 0

    for order in orders:
        if check_ordering(lookup, order):
            middle = len(order) // 2
            total += int(order[middle])

    return total


def fix_ordering(lookup, order):
    fixed_order = []
    remaining = set(order)

    while len(fixed_order) < len(order):
        diff = set()

        for page in remaining:
            if page in lookup:
                 diff |= lookup[page]

        allowed = remaining - diff

        next_page = list(allowed)[0]

        if len(allowed) > 1:
            print(allowed)

        fixed_order.append(next_page)
        remaining -= { next_page }

    return fixed_order
                

def part2(lookup, orders):
    total = 0

    for order in orders:
        if not check_ordering(lookup, order):
            fixed_order = fix_ordering(lookup, order)

            assert check_ordering(lookup, fixed_order)

            total += int(fixed_order[len(fixed_order) // 2])

    return total


print(part1(lookup, orderings))
print(part2(lookup, orderings))
