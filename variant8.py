arr = [3, 2, -7, -9, 1, 0, -2, 1, -2, 1, 2, -6, -7, -9, 0, 6, 1, 8, 4, 4, -1, 1]
k = 5

print("Масив:")
print(*arr)

negative = []
positive = []
greater = []

for x in arr:
    if x < 0 and x < k:
        negative.append(x)
    elif x >= 0 and x < k:
        positive.append(x)
    elif x > k:
        greater.append(x)

result = negative + positive + [str(k) + "*"] + greater

print("Результат:")
print(*result)