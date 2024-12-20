from math import inf
from heapq import heappop, heappush
from functools import cache

example = False

input_file = "./example.txt" if example else "./input.txt"

with open(input_file) as f:
    grid = f.read().splitlines()

n = len(grid)
m = len(grid[0])

walls = set()

S = -1
E = -1

for y in range(len(grid)):
    for x in range(len(grid[0])):
        match grid[y][x]:
            case '#':
                walls.add(x + 1j*y)
            case 'S':
                S = x + 1j*y
            case 'E':
                E = x + 1j*y

assert S != -1 and E != -1
dirs = [1, -1, 1j, -1j]

def reachable(S, max_depth):
    global walls
    reachable = set()

    Q = [(S, 0)]

    seen = set()

    while Q:
        z, depth = Q[0]
        Q = Q[1:]

        if z in seen:
            continue

        seen.add(z)

        for dz in dirs:
            w = z + dz

            if w in seen:
                continue
            if not (0 <= w.real < m and 0 <= w.imag < n):
                continue

            if w not in walls:
                assert depth < max_depth
                reachable.add((w, depth))

            if depth + 1 < max_depth:
                Q.append((w, depth+1))

    return reachable

def find_cheats(S, curr_score, optimum, reachables):
    global walls, lookup

    # Q = [(S, 1)]
    res = 0

    for (w, depth) in reachables[S]:
        if w not in lookup:
            continue
        possible_score = curr_score + depth + lookup[w]

        advantage = optimum - possible_score

        if advantage >= 100:
            res += 1
    return res


def dijkstra(S, E, cheating_allowed=True, all_dists=False, part2=False):
    global walls, lookup
    if cheating_allowed:
        legal_dists = dijkstra(S, E, cheating_allowed=False, all_dists=True)

        legal_optimum = legal_dists[E]

        reachables = dict()
        for w in legal_dists.keys():
            assert w not in walls
            if part2:
                reachables[w] = reachable(w, 20)
            else:
                reachables[w] = reachable(w, 2)


    # entries are: (score, entry_count, pos, cheat)
    Q = [(0, 0, S)]
    seen = set()
    counted = set()
    distances = dict()

    entry_count = 1

    result = 0

    while Q:
        score, _, z = heappop(Q)

        if not cheating_allowed:
            if z not in distances:
                distances[z] = score

        if z == E:
            if cheating_allowed:
                return result
            if not all_dists:
                return score

        seen.add(z)

        if cheating_allowed and z not in counted:
            if part2:
                result += find_cheats(z, score, legal_optimum, reachables)
            else:
                result += find_cheats(z, score, legal_optimum, reachables)
            counted.add(z)

        for dz in dirs:
            w = z + dz
            if not (0 <= w.real < m and 0 <= w.imag < n):
                continue

            next_score = score + 1

            if w in seen:
                continue

            seen.add(w)

            if w in walls:
                continue

            heappush(Q, (next_score, entry_count, w))
            entry_count += 1

    if not cheating_allowed:
        return distances if all_dists else None
    return result

lookup = dijkstra(E, None, cheating_allowed=False, all_dists=True, part2=False)

def solve(S, E, part2=False):
    return dijkstra(S, E, cheating_allowed=True, all_dists=False, part2=part2)

print(solve(S, E))
print(solve(S, E, part2=True))

