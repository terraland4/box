"""
n = 500
dz = 1/n
pts = 0

i = 0
while i <= n:
    x = dz * i
    j = 0
    while j <= n:
        y = dz * j
        if y <= x and y >= x**2:
            pts = pts + 1
        j = j + 1
    i = i + 1
s = pts/(n + 1)**2
print("Площадь фигуры:", s)

#________________________________________________
print("Сумма натуральных чисел")
n = 100
text  = "1 + 2 + ... + " + str(n) + " ="

s = 0
for i in range(1, n+1):
    s += i
print(text, s)

print(sum(range(1, n + 1)))
"""
#____________________________________________________

txt = "Python"

i = 1
for s in txt:
    t = str(i) + "-я буква:"
    print(t, s)
    i = i + 1
print("Работа программы завершина!")

