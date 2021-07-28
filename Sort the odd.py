# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# You will be given an array of numbers.
# You have to sort the odd numbers in ascending order
# while leaving the even numbers at their original positions.
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

def sort_array(source_array):
    if not source_array:
        return source_array
    else:
        odd_numbers = []
        for i in range(0, len(source_array)):
            if (source_array[i] % 2) == 1:
                odd_numbers.append(source_array[i])
                odd_numbers.sort()
        j = 0
        for i in range(0, len(source_array)):
            if (source_array[i] % 2) == 1:
                source_array[i] = odd_numbers[j]
                j += 1
        return source_array


sort_array([5, 3, 2, 8, 1, 4])
sort_array([5, 3, 1, 8, 0])
sort_array([])
sort_array([7, 1])
sort_array([5, 8, 6, 3, 4])
sort_array([9, 8, 7, 6, 5, 4, 3, 2, 1, 0])
