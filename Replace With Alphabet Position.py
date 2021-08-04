# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# Welcome.
# In this kata you are required to, given a string, replace every letter with its position in the alphabet.
# If anything in the text isn't a letter, ignore it and don't return it.
# "a" = 1, "b" = 2, etc.
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

def alphabet_position(text):
    alphabet_list = []
    for i in range(0, len(text)):
        if text[i].isalpha():
            list_of_letters = list(text.lower())
            alphabet_list.append(ord(list_of_letters[i]) - 96)
    string_ints = [str(int) for int in alphabet_list]
    string_of_ints = ' '.join(string_ints)
    return string_of_ints


alphabet_position("The sunset sets at twelve o' clock.")
alphabet_position("The narwhal bacons at midnight.")
