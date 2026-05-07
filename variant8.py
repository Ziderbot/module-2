
arr = list(map(int, input("Введіть 22 числа через пробіл: ").split()))

# Введення числа k
k = int(input("Введіть число k: "))

print("\nМасив:")
for num in arr:
    print(num, end=" ")

print("\n\nРезультат:")

# 1. Від'ємні числа
for num in arr:
    if num < 0:
        print(num, end=" ")

# 2. Додатні числа менші за k
for num in arr:
    if num > 0 and num < k:
        print(num, end=" ")

# 3. Число k із зірочкою
print(f"{k}*", end=" ")

# 4. Числа більші за k
for num in arr:
    if num > k:
        print(num, end=" ")