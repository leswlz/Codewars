# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# Introduction
# There is a war and nobody knows - the alphabet war!
# There are two groups of hostile letters.
# The tension between left side letters and right side letters was too high and the war began.
# Task
# Write a function that accepts fight string consists of only small letters and return who wins the fight.
# When the left side wins return Left side wins!, when the right side wins return Right side wins!,
# in other case return Let's fight again!.
# The left side letters and their power:
#  w - 4
#  p - 3
#  b - 2
#  s - 1
# The right side letters and their power:
#  m - 4
#  q - 3
#  d - 2
#  z - 1
# The other letters don't have power and are only victims.
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

def alphabet_war(fight):
    left_side = 0
    right_side = 0

    for i in range(0, len(fight)):
        if fight[i] in {"w", "p", "b", "s"}:
            left_side += powers(fight[i])
        elif fight[i] in {"m", "q", "d", "z"}:
            right_side += powers(fight[i])

    if left_side > right_side:
        return "Left side wins!"
    elif left_side < right_side:
        return "Right side wins!"
    else:
        return "Let's fight again!"


def powers(x):
    return {
        "w": 4, "p": 3, "b": 2, "s": 1,  # the left side letters and their powers
        "m": 4, "q": 3, "d": 2, "z": 1,  # the right side letters and their powers
    }[x]


alphabet_war("z")
alphabet_war("zdqmwpbs")
alphabet_war("wm")
alphabet_war("wq")
alphabet_war("zzzzs")
alphabet_war("wwwwww")
