def linear_search_iterative(elements, key):
    """
        An index, i, where A[i] = k.
        If there is no such i, then
        NOT_FOUND.
    """
    for idx, value in enumerate(elements):
        if key == value:
            return idx
    return "Not Found"


def linear_search_recursive(elements, low, high, key):
    if high < low:
        return "Not Found"

    if elements[low] == key:
        return low

    return linear_search_recursive(elements, low + 1, high, key)


def main():
    elements = ['nahid', 'hassan', 'mahin', 'mony', 'joe', 'doe']
    out = linear_search_iterative(elements, 'mahin')
    print(out)
    out = linear_search_recursive(elements, 0, len(elements)-1, 'mpahin')
    print(out)


if __name__ == "__main__":
    main()
