def bfunc(text):
    wordlist = text.lower().split()
    print (wordlist)
    first_word_index = wordlist[0]
    second_word_index = wordlist[1]
    return first_word_index[0] == second_word_index[0]