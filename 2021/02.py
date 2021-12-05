instructions = []
for line in open('02.txt'):
    parts = line.split()
    direction = parts[0]
    step = int(parts[1])
    instructions.append([direction, step])

h1 = 0
d1 = 0

h2 = 0
d2 = 0
aim = 0

for [direction, step] in instructions:
    if direction == 'up':
        d1 -= step
        aim -= step
        continue
    if direction == 'down':
        d1 += step
        aim += step
        continue
    if direction == 'forward':
        h1 += step
        h2 += step
        d2 += aim * step

print(h1 * d1)  # 2150351
print(h2 * d2)  # 1842742223
