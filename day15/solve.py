example = True

movement_table = {
    "<": (-1, 0),
    ">": (1, 0),
    "^": (0, -1),
    "v": (0, 1)
}

input_file = "./input.txt" if example else "./input.txt"

with open(input_file) as f:
    grid, movements = f.read().split("\n\n")

    grid = grid.strip().splitlines()
    movements = [movement_table[c] for c in movements.strip().replace("\n", "")]

def solve1(grid, movements):
    n = len(grid)
    m = len(grid[0])

    boxes = set()
    walls = set()
    px, py = (-1, -1)
    for y in range(n):
        for x in range(m):
            obj = grid[y][x]
            if obj == '@':
                px, py = (x, y)
            elif obj == '#':
                walls.add((x, y))
            elif obj == 'O':
                boxes.add((x, y))

    for (dx, dy) in movements:
        nx, ny = px + dx, py + dy

        if (nx, ny) in boxes:
            bx, by = (nx + dx, ny + dy)
            while (bx, by) in boxes:
                bx, by = (bx + dx, by + dy)
            if (bx, by) not in walls:
                boxes -= { (nx, ny) }
                boxes.add((bx, by))
            else:
                continue
        elif (nx, ny) in walls:
            continue
        px, py = nx, ny

    total = 0

    for (bx, by) in boxes:
        total += 100*by + bx

    return total


def solve2(grid, movements):
    n = len(grid)
    m = len(grid[0])

    boxes = set()
    walls = set()
    px, py = (-1, -1)
    for y in range(n):
        actual_x = 0
        for x in range(m):
            obj = grid[y][x]
            if obj == '@':
                px, py = (actual_x, y)
            elif obj == '#':
                walls.add((actual_x, y))
                walls.add((actual_x + 1, y))
            elif obj == 'O':
                boxes.add((actual_x, y))
            actual_x += 2

    for (dx, dy) in movements:
        nx, ny = px + dx, py + dy

        if (nx, ny) in walls:
            continue
        elif (dx, dy) == (1, 0):
            if (nx, ny) in boxes:
                new_boxes = { (nx + 1, ny) }
                to_move = { (nx, ny) }
                bx, by = nx + 2, ny
                while (bx, by) in boxes:
                    new_boxes.add((bx+1, by))
                    to_move.add((bx, by))
                    bx += 2
                if (bx, by) not in walls:
                    for (x, y) in new_boxes:
                        boxes -= to_move
                        boxes |= new_boxes
                else:
                    continue
            px, py = nx, ny
        elif (dx, dy) == (-1, 0):
            assert (nx, ny) not in boxes # should be impossible
            if (nx - 1, ny) in boxes:
                new_boxes = { (nx - 2, ny) }
                to_move = { (nx - 1, ny) }

                bx, by = nx - 3, ny
                while (bx, by) in boxes:
                    new_boxes.add((bx - 1, by))
                    to_move.add((bx, by))
                    bx -= 2
                if (bx+1, by) not in walls:
                    for (x, y) in new_boxes:
                        boxes -= to_move
                        boxes |= new_boxes
                else:
                    continue
            px, py = nx, ny
        else:
            if (nx, ny) in boxes:
                frontier = [(nx, ny)]
            elif (nx - 1, ny) in boxes:
                frontier = [(nx-1, ny)]
            else:
                px, py = nx, ny
                continue

            to_move = set()

            while frontier:
                bx, by = frontier[0]
                to_move.add((bx, by))
                frontier = frontier[1:]

                if (bx, by + dy) in boxes:
                    frontier.append((bx, by + dy))
                if (bx - 1, by + dy) in boxes:
                    frontier.append((bx - 1, by + dy))
                if (bx + 1, by + dy) in boxes:
                    frontier.append((bx + 1, by + dy))
                if (bx, by + dy) in walls or (bx + 1, by + dy) in walls:
                    # Can't move anything
                    break
            else:
                new_boxes = set()
                for (bx, by) in to_move:
                    new_boxes.add((bx, by + dy))
                boxes -= to_move
                boxes |= new_boxes
                px, py = nx, ny
            continue


    total = 0

    for (bx, by) in boxes:
        total += 100*by + bx

    return total


print(solve1(grid, movements))
print(solve2(grid, movements))

