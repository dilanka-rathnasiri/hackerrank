
"""
1. get full list digits
2. get full list of letters in lowercase
3. combine two list
4. delete each character of the given string in combined list
"""

import string

def missingCharacters(s):
    digits = list(map(str, range(10)))
    letters = list(string.ascii_lowercase)
    all_list = [*digits, *letters]
    result = [i for i in all_list if i not in s]
    return "".join(result)


def main():
    s = "798abcd"
    result = missingCharacters(s)
    print(result)

if __name__ == "__main__":
    main()