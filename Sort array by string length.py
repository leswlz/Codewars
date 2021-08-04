# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# Write a function that takes an array of strings as an argument
# and returns a sorted array containing the same strings, ordered from shortest to longest.
# For example, if this array were passed as an argument:
# ["Telescopes", "Glasses", "Eyes", "Monocles"]
# Your function would return the following array:
# ["Eyes", "Glasses", "Monocles", "Telescopes"]
# All of the strings in the array passed to your function will be different lengths,
# so you will not have to decide how to order multiple strings of the same length.
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

def sort_by_length(arr):
    sorted_arr = sorted(arr, key=len)
    return sorted_arr


sort_by_length(["beg", "life", "i", "to"])
sort_by_length(["", "moderately", "brains", "pizza"])
sort_by_length(["longer", "longest", "short"])
sort_by_length(["dog", "food", "a", "of"])
sort_by_length(["", "dictionary", "eloquent", "bees"])
sort_by_length(["a longer sentence", "the longest sentence", "a short sentence"])
