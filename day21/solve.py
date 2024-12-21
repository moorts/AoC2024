from itertools import permutations
from collections import defaultdict

def precompute_numeric_keypad():
    graph = {
        '7': 0,
        '8': 1,
        '9': 2,
        '4': 1j,
        '5': 1 + 1j,
        '6': 2 + 1j,
        '1': 2j,
        '2': 1 + 2j,
        '3': 2 + 2j,
        '0': 1 + 3j,
        'A': 2 + 3j,
    }

    shortest_paths = {}

    for start, end in permutations(graph.keys(), 2):
        d = graph[end] - graph[start]

        path = ''
        if d.real < 0 and (graph[end].real != 0 or graph[start].imag != 3):
            path += '<' * int(-d.real)

        if d.imag < 0:
            path += '^' * int(-d.imag)

        if d.real > 0 and (graph[start].real == 0 and graph[end].imag == 3):
            path += '>' * int(d.real)

        if d.real < 0 and (graph[end].real == 0 and graph[start].imag == 3):
            path += '<' * int(-d.real)

        if d.imag > 0:
            path += 'v' * int(d.imag)

        if d.real > 0 and (graph[start].real != 0 or graph[end].imag != 3):
            path += '>' * int(d.real)

        shortest_paths[(start, end)] = path

    for c in graph.keys():
        shortest_paths[(c, c)] = ''

    return shortest_paths


def precompute_directional_keypad():
    graph = {
        '^': 1,
        'A': 2,
        '<': 1j,
        'v': 1 + 1j,
        '>': 2 + 1j,
    }

    shortest_paths = {}

    for start, end in permutations(graph.keys(), 2):
        d = graph[end] - graph[start]

        path = ''

        if d.real < 0 and (graph[end].real != 0 or graph[start].imag != 0):
            path += '<' * int(-d.real)

        if d.real > 0 and (graph[start].real == 0 and graph[end].imag == 0):
            path += '>' * int(d.real)

        if d.imag > 0:
            path += 'v' * int(d.imag)

        if d.imag < 0:
            path += '^' * int(-d.imag)

        if d.real < 0 and (graph[end].real == 0 and graph[start].imag == 0):
            path += '<' * int(-d.real)

        if d.real > 0 and (graph[start].real != 0 or graph[end].imag != 0):
            path += '>' * int(d.real)


        shortest_paths[(start, end)] = path

    for c in graph.keys():
        shortest_paths[(c, c)] = ''

    return shortest_paths


numpad = precompute_numeric_keypad()
dirpad = precompute_directional_keypad()

example = False

input_file = "./example.txt" if example else "./input.txt"

with open(input_file) as f:
    codes = f.read().splitlines()

def solve(codes, part2=False):
    global numpad, dirpad

    result = 0

    for code in codes:
        num_dirpads = 25 if part2 else 2

        length = 0

        prev = 'A'

        for c in code:
            keypresses = numpad[(prev, c)] + 'A'
            prev = c

            segments = defaultdict(int)
            segments[keypresses] = 1

            for _ in range(num_dirpads):
                new_segments = defaultdict(int)
                for segment in segments.keys():
                    curr = 'A'
                    for k in segment:
                        expanded = dirpad[(curr, k)] + 'A'
                        curr = k

                        new_segments[expanded] += segments[segment]
                segments = new_segments

            length += sum([len(segment) * l for (segment, l) in segments.items()])

        numeric_part = int(code[:-1])
        complexity = length * numeric_part

        result += complexity

    return result

print(solve(codes))
print(solve(codes, part2=True))
