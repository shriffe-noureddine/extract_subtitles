import operator
from wordsClass import wordsClass
# curl https:///bootstrap.pypa.io/get-pip.py -o get-pip.py
# python get-pip.py
# pip install pyperclip
# =CHAR(39) & A1 & CHAR(39) & CHAR(44) for excel
import pyperclip
sub = pyperclip.paste()

words = sub.lower().split()
# class wordsClass:
#     words = ['the', 'he', 'she']
myWords = wordsClass()

def clean_up_list(list_words):
    dec_words = {}
    for word in list_words:
        symbols = ['</i>', '<i>', ',', '"', ')', '.', '/',
                   '\\', '(', '*', '&', '^', '%', '$',
                   '#', '@', '!', '?', '>', '<', '|',
                   ':', '}', '{', '1', '2', '3', '4',
                   '5', '6', '7', '8', '9', '0', '-',
                   '♪', '=', '[', ']', ';', '+', '_']

        for i in range(0, len(symbols)):
            word = word.replace(symbols[i], '')
        if len(word) > 1:
            dec_words.setdefault(word, 0)
            dec_words[word] += 1

        for known_word in myWords.words:
            if known_word in dec_words:
                del dec_words[known_word]

    for k, v in sorted(dec_words.items(), key=operator.itemgetter(1)):
        print(k, v)



clean_up_list(words)