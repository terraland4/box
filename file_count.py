import requests
from bs4 import BeautifulSoup


"""
for i in range(len(filenames)):
    print(i)

    print(filenames[i])

    filename = filenames[i]
"""


def count_words(filename):
    """Подсчет приблизительного количества строк в файле."""
try:

    with open(filename) as f_obj:
        contents = f_obj.read()



except FileNotFoundError:
    msg = "Sorry, the file " + filename + " does not exist."
    print(msg)
else:
    # Подсчет приблизительного количества строк в файле.
    words = contents.split()
    num_words = len(words)
    print("The file " + filename + " has about " + str(num_words) + " words.")

filenames = ['alice.txt', 'mobydic.txt', 'little_girl.txt']

for filename in filenames:
    count_words(filename)
    print(filename)


count_words(filename)

