# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# Simple, given a string of words, return the length of the shortest word(s).
# String will never be empty and you do not need to account for different data types.
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

def find_short(sentence):
    return len(min(sentence.split(), key=len))


find_short("bitcoin take over the world maybe who knows perhaps")
find_short("turns out random test cases are easier than writing out basic ones")
find_short("lets talk about javascript the best language")
find_short("i want to travel the world writing code one day")
find_short("Lets all go on holiday somewhere very cold")
find_short("Let's travel abroad shall we")
