import copy

with open("input.txt") as f:
    disk_map = [int(x) for x in f.read().strip()]

def part1(disk_map):
    # I do inplace modification (for reasons)
    disk_map = copy.deepcopy(disk_map)

    front = 0
    front_file_idx = 0

    back = len(disk_map) - 1 if len(disk_map) % 2 == 1 else len(disk_map) - 2
    back_file_idx = len(disk_map) // 2

    checksum = 0
    position = 0

    while front <= back:
        if front % 2 == 0:
            for _ in range(disk_map[front]):
                checksum += position * front_file_idx
                position += 1
            front_file_idx += 1
        else:
            remaining = disk_map[front]

            while remaining:
                effective_space = min(remaining, disk_map[back])
                for _ in range(effective_space):
                    checksum += position * back_file_idx
                    position += 1

                remaining -= effective_space
                left_over = max(0, disk_map[back] - effective_space)

                if left_over:
                    disk_map[back] = left_over
                else:
                    back -= 2
                    back_file_idx -= 1
        front += 1

    return checksum
    
def compute_checksum(start, space, idx):
    return sum([idx * (start + i) for i in range(space)])

def part2(disk_map):
    free_segments = []
    files = []

    checksum = 0
    position = 0

    for i, space in enumerate(disk_map):
        if i % 2 == 0:
            file_idx = i // 2
            files.append((position, space))
        else:
            if space:
                free_segments.append((position, space))
        position += space


    for i, (position, required_space) in enumerate(files[::-1]):
        file_idx = len(files) - i - 1

        file_moved = False
        for j, (start, free_space) in enumerate(free_segments):
            if start >= position:
                break

            if free_space >= required_space:
                checksum += compute_checksum(start, required_space, file_idx)
                if free_space > required_space:
                    free_segments[j] = (start + required_space, free_space - required_space)
                else:
                    del free_segments[j]

                file_moved = True
                break
        if not file_moved:
            # File stays in position
            checksum += compute_checksum(position, required_space, file_idx)

    return checksum


print(part1((disk_map)))
print(part2(disk_map))
