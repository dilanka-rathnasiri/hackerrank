def extraLongFactorials(n):
    fact = 1
    for i in range(n, 1, -1):
        fact *= i
    return fact


def main():
    result = extraLongFactorials(30)
    print(result)


if __name__ == "__main__":
    main()
