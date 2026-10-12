data = []
while len(data) < 6:
    data += input().split()
a, b, i, j, x, y = map(float, data[:6])
print(f"{(a - b) * i / j - (x + y):.3f}")