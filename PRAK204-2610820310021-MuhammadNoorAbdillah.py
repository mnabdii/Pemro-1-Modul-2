data = []
while len(data) < 2:
    data += input().split()
r, t = map(float, data[:2])
pi = 22 / 7
print(f"Volume = {pi * r * r * t:.2f}")
print(f"Luas = {2 * pi * r * (r + t):.2f}")
print(f"Keliling = {2 * pi * r:.2f}")