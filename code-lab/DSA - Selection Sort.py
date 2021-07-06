elements = [8, 4, 2, 5, 2]


def selection_sort(elements):
    n = len(elements)

    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            # find the index
            if elements[j] < elements[min_idx]:
                min_idx = j
        # swap between index i value and min_idx value
        elements[min_idx], elements[i] = elements[i], elements[min_idx]

    return elements


def main():
    out = selection_sort(elements)
    print(out)


if __name__ == "__main__":
    main()
