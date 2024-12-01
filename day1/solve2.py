from collections import Counter

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
freqs = Counter(right)

similarity = 0

for a in left:
    similarity += a * freqs[a]

print(similarity)




