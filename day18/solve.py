from heapq import heappush, heappop
example = False

input_file = "./example.txt" if example else "./input.txt"

with open(input_file) as f:
    positions = [x.split(",") for x in f.read().splitlines()]
    positions = [int(x) + 1j*int(y) for x,y in positions]

def neighbors(z):
    n = 7 if example else 71
    return [z + w for w in [1, -1, 1j, -1j] if 0 <= (z + w).imag < n and 0 <= (z + w).real < n]

def solve(positions, num_bytes=1024):
    obstacles = set(positions[:num_bytes])

    target = 6 + 6j if example else 70 + 70j

    Q = [(0, 0, 0)]
    seen = set()
    prev = dict()

    entry_count = 1

    while Q:
        dist, _, z = heappop(Q)

        if z == target:
            return dist, prev

        for w in neighbors(z):
            if w in prev.keys() or w in obstacles:
                continue

            heappush(Q, (dist + 1, entry_count, w))
            entry_count += 1
            seen.add(w)
            prev[w] = z

    return None

def get_path(prev, start, target):
    path = {start, target}
    curr = target
    while curr != start:
        curr = prev[curr]
        path.add(curr)

    return path

def solve2(positions, num_bytes):
    _, prev = solve(positions, num_bytes)

    target = 6 + 6j if example else 70 + 70j

    path = get_path(prev, 0, target)

    for i in range(num_bytes, len(positions)):
        if positions[i] in path:
            if not (res := solve(positions, num_bytes=i+1)):
                return positions[i]
            path = get_path(res[1], 0, target)

    return -1
                

print(solve(positions, num_bytes=1024)[0])

print(solve2(positions, num_bytes=1024))
