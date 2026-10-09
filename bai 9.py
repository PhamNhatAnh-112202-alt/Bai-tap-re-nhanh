n = int(input())
if n <= 5:
    tien = n * 10000
else:
    tien = 5 * 10000 + (n - 5) * 5000
print(tien)
