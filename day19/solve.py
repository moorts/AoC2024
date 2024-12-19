from functools import cache

example = False

input_file = "./example.txt" if example else "./input.txt"

with open(input_file) as f:
    towels, designs = f.read().split("\n\n")

    towels = towels.strip().split(", ")
    designs = designs.strip().splitlines()



@cache
def is_possible(design, part2=False):
    global towels
    designs = 0
    for towel in towels:
        if towel == design:
            if not part2: return True
            designs += 1

        elif len(towel) > len(design):
            continue
        
        elif design[:len(towel)] == towel:
            if x := is_possible(design[len(towel):], part2=part2):
                if not part2: return True
                designs += x

    if not part2:
        return False

    return designs

def solve(designs, part2=False):
    return sum([is_possible(design, part2=part2) for design in  designs])


print(solve(designs))
print(solve(designs, part2=True))
