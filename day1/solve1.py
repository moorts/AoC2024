with open("./input.txt") as f:
    data = f.read()
    lines = data.splitlines()

    left = []
    right = []

    for line in lines:
        a, b = line.split("   ")

        left.append(int(a))
        right.append(int(b))

left = sorted(left)
right = sorted(right)

total = 0

for a, b in zip(left, right):
    total += abs(a - b)

print(total)




