"""
def my_exp(x, n):
    s = 0
    q = 1
    for k in range(n + 1):
        s += q
        q *= x/(k + 1)
    return s

x = 1
for n in range(11):
    print("n =", n, "->", my_exp(x, n))
"""

def print_text(txt = "Значение аргумента по умолчанию."):
    print(txt)

def show_args(a, b = "Второй аргумент неуказан."):
    print(a, b)

def my_func(x = "1-й аргумент x.", y = "2-й аргумент y.",):
    print(x, y)

print_text("Аргумент указан явно.")
print_text()

show_args("Первый аргумент.", "Второй аргумент.")
show_args("Первый аргумент.")

my_func()
my_func("Один из аргументов.")
my_func(y = "Один из аргументов.")

def get_sum(*nums):
    s = 0
    for a in nums:
        s += a
    return s

print(get_sum(1, 3, 5, 11))


def my_func(txt):
    print("Функция my_func:", txt)

new_func = my_func

new_func("вызов через new_func.")
print(my_func("вызов через new_func."))
