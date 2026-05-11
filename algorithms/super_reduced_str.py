"""
1. Get string as a list
2. Iterate trough a string one character by character with while loop
3. if each character is equal to adjusted character delete both
"""


def superReducedString(s):
    chars = list(s)
    i = 0
    while True:
        if len(chars) == 0:
            return "Empty String"
        elif i + 1 >= len(chars):
            return "".join(chars)
        elif chars[i] == chars[i + 1]:
            del chars[i : i + 2]
            if i != 0:
                i -= 1
        else:
            i += 1


def main():
    s = "aaabccddd"
    result = superReducedString(s)
    print(result)


if __name__ == "__main__":
    main()
