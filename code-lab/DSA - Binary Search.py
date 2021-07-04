def binary_search_iterative(elements, key):
    low = 0
    high = len(elements) - 1

    while low <= high:
        mid = (low + high) // 2
        if elements[mid] == key:
            # wow! found, return the mid
            return mid
        elif elements[mid] < key:
            # change low
            low = mid + 1
        else:
            # change high
            high = mid - 1
    return low - 1


def binary_search_recursive(elements, low, high, key):
    if high < low:
        return low - 1

    mid = int(low + ((high - low) / 2))
    if key == elements[mid]:
        return mid
    elif key < elements[mid]:
        return binary_search_recursive(elements, low, mid-1, key)
    else:
        return binary_search_recursive(elements, mid+1, high, key)


def main():
    elements = [3, 4, 4, 8, 10, 10, 14, 20, 34]
    out = binary_search_recursive(elements, 0, len(elements) - 1, 30)
    print(out)

    out = binary_search_iterative(elements, 30)
    print(out)


if __name__ == "__main__":
    main()
