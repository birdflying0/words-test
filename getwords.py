#!/usr/bin/env python3

import pandas as pd

def  get_words(filename):
    word_list = []
    data = pd.read_excel(filename)
    english = data["English"]
    chinese = data["Chinese"] 
    for i in range(0, len(english)) :
        word_list.append([ english[i], chinese[i] ] )
    return word_list


if __name__ == "__main__":
    words = get_words("dict.xlsx")
    print(words)

