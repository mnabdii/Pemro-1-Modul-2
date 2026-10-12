import math
data = []
while len(data) < 2:
    data += input().split()
A, B = map(int, data[:2])
alas = round(math.sqrt(B * B - A * A))
print(f"Alas = {alas} cm")
print(f"Tinggi = {A} cm")
print(f"Keliling = {alas + A + B} cm")
print(f"Luas = {alas * A // 2} cm^2")