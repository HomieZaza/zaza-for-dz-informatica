n = 0
s = 0
while True:
    a = int(input("Введите число:  "))
    if a == 0:
        break
    if len(str(a)) == 2:
        n += 1
        s += a
if n == 0:
    print("NOPE")
else:
    print(s/n)
