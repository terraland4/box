
filename = 'alice.txt'

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



count_words(filename)