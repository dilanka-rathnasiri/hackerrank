"""
A. understand
iterate using loop
and go loop forward
"""


def pickingNumbers(a):
    max_len = 0
    for i in range(len(a)):
        sub_a = [a[j] for j in range(len(a)) if a[j] in (a[i], a[i] + 1)]
        if len(sub_a) > max_len:
            max_len = len(sub_a)
    return max_len


def main():
    a = [4, 6, 5, 3, 3, 1]
    result = pickingNumbers(a)  # expected=3
    print(result)


if __name__ == "__main__":
    main()
