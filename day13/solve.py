from z3 import *
from parse import compile

btn_template = compile("Button {}: X+{}, Y+{}")
prize_template = compile("Prize: X={}, Y={}")

def parse_btn(button):
    _, x, y = btn_template.parse(button)

    return x, y

def parse_machine(machine):
    rows = machine.splitlines()

    dx_a, dy_a = parse_btn(rows[0])
    dx_b, dy_b = parse_btn(rows[1])
    prize_x, prize_y = prize_template.parse(rows[2])

    return ((int(dx_a), int(dy_a)), (int(dx_b), int(dy_b)), (int(prize_x), int(prize_y)))

with open("./input.txt") as f:
    data = f.read()

    machines = data.split("\n\n")


machines = [parse_machine(machine) for machine in machines]

def solve(machines, part2=False):
    total = 0
    for ((dx_a, dy_a), (dx_b, dy_b), (prize_x, prize_y)) in machines:
        if part2:
            prize_x = prize_x + 10000000000000
            prize_y = prize_y + 10000000000000
        s = Optimize()
        a = Int('a')
        b = Int('b')

        s.add(dx_a*a + dx_b*b == prize_x, dy_a*a + dy_b*b == prize_y)
        s.minimize(3*a + b)

        if s.check() == sat:
            a_val = s.model()[a].as_long()
            b_val = s.model()[b].as_long()
            total += 3 * a_val + b_val
    return total

print(solve(machines))
print(solve(machines, part2=True))
