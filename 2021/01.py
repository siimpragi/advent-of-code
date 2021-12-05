measurements = [int(m) for m in open('01.txt')]

n1 = 0
n2 = 0
for i in range(len(measurements)):
    if i > 0 and measurements[i] > measurements[i - 1]:
        n1 += 1
    if i > 2 and measurements[i - 2] + measurements[i - 1] + measurements[i] > measurements[i - 3] + measurements[i - 2] + measurements[i - 1]:
        n2 += 1
print(n1)  # 1387
print(n2)  # 1362
