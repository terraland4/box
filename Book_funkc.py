
def your_name():
    print("Добрый день!")
    name = input("Как Вас зовут? ")
    return name

def say_hello(txt):
    print("Здравствуйте,", str(txt) + "!")

my_name = your_name()
say_hello(my_name)