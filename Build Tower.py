# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# Build Tower by the following given argument:
# number of floors (integer and always greater than 0).
# Tower block is represented as *
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

def tower_builder(n_floors):
    list = [None] * n_floors
    for i in range(1, n_floors + 1):
        list[i - 1] = (" " * (n_floors - i) + "*" * (i + (i - 1)) + " " * (n_floors - i))
    return list


tower_builder(1)
tower_builder(2)
tower_builder(3)
