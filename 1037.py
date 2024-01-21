b = 0
while True:
    a = int(input("Введите число:  "))
    if a == 0:
        break
    if a % 9 == 0 or a % 5 == 0:
        b += 1
print(b)
