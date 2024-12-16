import heapq
from math import inf

example = False

input_file = "./example2.txt" if example else "./input.txt"

with open(input_file) as f:
    maze = f.read().splitlines()

def dijkstra(Q, start, target, walls, part2=False):
    entry_count = 0
    seen = dict()
    shortest_path = -1

    while Q:
        score, _, curr, direction = heapq.heappop(Q)
        assert score != inf
        if curr == target:
            if not part2:
                return score

            if shortest_path == -1:
                shortest_path = score

        if shortest_path != -1 and score > shortest_path:
            break

        for rotation, num_rotations in [(1, 0), (1j, 1), (-1j, 1), (-1, 2)]:
            next_space = curr + rotation * direction
            next_score = score + 1 + 1000*num_rotations

            ident = (next_space, rotation * direction)
            if next_space in walls:
                continue
            if ident in seen:
                old_score, prevs = seen[ident]
                if next_score < old_score:
                    seen[ident] = (next_score, [(curr, direction)])
                elif next_score == old_score:
                    seen[ident] = (old_score, prevs + [(curr, direction)])
                else:
                    continue
            else:
                seen[ident] = (next_score, [(curr, direction)])
            entry_count += 1
            heapq.heappush(Q, (next_score, entry_count, next_space, rotation * direction))

    res = 1
    Q = []
    processed = set()
    counted_tiles = set()
    for direction in [1, 1j, -1j, -1]:
        Q.append((target, direction))
    while Q:
        p = Q[0]
        Q = Q[1:]
        if p not in seen:
            continue
        _, prevs = seen[p]
        for u in prevs:
            if u in processed:
                continue
            tile, _ = u
            if tile not in counted_tiles:
                res += 1
            if u == start:
                continue
            counted_tiles.add(tile)
            processed.add(u)
            Q.append(u)

    return res

def solve(maze, part2=False):
    n = len(maze)
    m = len(maze[0])

    walls = set()

    p, target = -1, -1

    Q = []

    entry = 100000
    for y in range(n):
        for x in range(m):
            if maze[y][x] == '#':
                walls.add(x + 1j*y)
                continue
            if maze[y][x] == 'S':
                p = x + 1j*y
                heapq.heappush(Q, (0, 0, p, 1))
                continue
            if maze[y][x] == 'E':
                target = x + 1j*y
            heapq.heappush(Q, (inf, entry, x + 1j*y, 1))
            entry += 1

    assert p != -1 and target != -1

    return dijkstra(Q, p, target, walls, part2=part2)


print(solve(maze))
print(solve(maze, part2=True))
