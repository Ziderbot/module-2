
arr = list(map(int, input("Введіть 22 числа через пробіл: ").split()))


k = int(input("Введіть число k: "))

print("\nМасив:")
for num in arr:
    print(num, end=" ")

print("\n\nРезультат:")


for num in arr:
    if num < 0:
        print(num, end=" ")

for num in arr:
    if num > 0 and num < k:
        print(num, end=" ")

print(f"{k}*", end=" ")

for num in arr:
    if num > k:
        print(num, end=" ")