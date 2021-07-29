# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# The new "Avengers" movie has just been released!
# There are a lot of people at the cinema box office standing in a huge line.
# Each of them has a single 100, 50 or 25 dollar bill. An "Avengers" ticket costs 25 dollars.
# Vasya is currently working as a clerk. He wants to sell a ticket to every single person in this line.
# Can Vasya sell a ticket to every person and give change if he initially has no money
# and sells the tickets strictly in the order people queue?
# Return YES, if Vasya can sell a ticket to every person and give change with the bills he has at hand at that moment.
# Otherwise return NO.
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

def tickets(people):
    cash_desk = []
    for i in range(0, len(people)):
        if people[i] == 25:
            cash_desk.append(25)
        elif people[i] == 50:
            if 25 in cash_desk:
                cash_desk.remove(25)
                cash_desk.append(50)
            else:
                return "NO"
        elif people[i] == 100:
            if 25 in cash_desk and 50 in cash_desk:
                cash_desk.remove(25)
                cash_desk.remove(50)
                cash_desk.append(100)
            elif cash_desk.count(25) == 3:
                cash_desk.remove(25)
                cash_desk.remove(25)
                cash_desk.remove(25)
                cash_desk.append(100)
            else:
                return "NO"
    return "YES"


tickets([25, 25, 50])
tickets([25, 100])
tickets([25, 25, 50])
tickets([25, 100])
tickets([25, 25, 50, 50, 100])
