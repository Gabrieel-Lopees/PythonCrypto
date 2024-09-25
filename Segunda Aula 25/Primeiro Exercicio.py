f = open('dictionary.txt', 'r')
words = [word.strip() for word in f]
f.close()