# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# In this kata you will create a function that takes a list of non-negative integers and strings
# and returns a new list with the strings filtered out.
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

def filter_list(l):
    new_list = []
    for i in range(0, len(l)):
        is_integer = isinstance(l[i], int)
        if is_integer:
            new_list.append(l[i])
    return new_list

print(filter_list([1,2,'a','b']))
print(filter_list([1,'a','b',0,15]))
print(filter_list([1,2,'aasf','1','123',123]))
