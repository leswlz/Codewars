# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# Complete the solution so that the function will break up camel casing, using a space between words.
# Example
# "camelCasing"  =>  "camel Casing"
# "identifier"   =>  "identifier"
# ""             =>  ""
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

class Break_camelCase():
    def __init__(self):
        pass

    def solution(self, input_string):
        return "".join([" " + ch if ch.isupper() else ch for ch in input_string])

    def check_equality(self, result_string, expected_output_string):
        if result_string == expected_output_string:
            return True
        return False
