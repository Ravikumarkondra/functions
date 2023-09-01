# 3.Write a Python function to check whether a string is a pangram or not.
# Note : Pangrams are words or sentences containing every letter of the alphabet at least once.
# For example : "The quick brown fox jumps over the lazy dog".


def is_pangram(input_string):

    input_string = input_string.lower()
    

    letters_set = set()
    for char in input_string:
        if char.isalpha():
            letters_set.add(char)
    
    return len(letters_set) == 26

input_str = "The quick brown fox jumps over the lazy dog"
if is_pangram(input_str):
    print("The string is a pangram.")
else:
    print("The string is not a pangram.")
