def main():
    """
        Simple Program that takes two numbers as input and
        return the sum of this two numbers.
        >>> 2 3
        5
        >>> 59 2
        61
    """

    # map(function, iterative)
    nums = list(map(int, input().split()))
    # extract numbers
    a, b = nums

    # return some of two digits
    return a + b


if __name__ == "__main__":
    result = main()
    print(result)