# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# Task
# In this simple Kata your task is to create a function that turns a string into a Mexican Wave.
# You will be passed a string and you must return that string in an array
# where an uppercase letter is a person standing up.
# Rules
# 1. The input string will always be lower case but maybe empty.
# 2. If the character in the string is whitespace then pass over it as if it was an empty seat
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

def wave(string):
    if not string:
        return []
    else:
        wave_list = [None] * len(string)
        n_spaces = 0  # number of spaces
        for i in range(0, len(string)):
            word = ""
            for j in range(0, len(string)):
                if string[i].isspace():
                    n_spaces += 1
                    break
                elif i == j:
                    word += string[i].upper()
                else:
                    word += string[j]
            wave_list[i] = word
        for i in range(0, n_spaces):
            wave_list.remove("")
        return wave_list


wave("hello")
wave("codewars")
wave("two words")
wave(" gap ")
