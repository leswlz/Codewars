# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# Your task is to sort a given string.
# Each word in the string will contain a single number.
# This number is the position the word should have in the result.
# Note: Numbers can be from 1 to 9. So 1 will be the first word (not 0).
# If the input string is empty, return an empty string.
# The words in the input String will only contain valid consecutive numbers.
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

def order(sentence):
    if not sentence:
        return ""
    else:
        word_list = sentence.split()
        ordered_list = [None] * len(word_list)

        for i in range(0, len(ordered_list)):
            list_position = position(word_list[i])
            del ordered_list[list_position - 1]
            ordered_list.insert(list_position - 1, word_list[i])
        ordered_string = ' '.join([str(item) for item in ordered_list])
        return ordered_string


def position(word):
    for i in range(0, len(word)):
        if word[i].isdigit():
            return int(word[i])


order("is2 Thi1s T4est 3a")
order("4of Fo1r pe6ople g3ood th5e the2")
order("")
