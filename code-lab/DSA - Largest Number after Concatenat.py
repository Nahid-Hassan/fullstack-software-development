def largest_number_greedy(nums):
    res = []
    for _ in range(len(nums)):
        mx = max(nums)
        res.append(mx)
        nums.remove(mx)
    return ''.join([str(x) for x in res])


def lexicographical_large_number(nums):
    print(nums)
    temp = [str(num) for num in nums]
    res = []

    for _ in range(len(temp)):
        mx = max(temp)
        print(mx)
        res.append(mx)
        temp.remove(mx)
    return res


def main():
    nums = [8, 1, 9, 3, 2]
    large_number = largest_number_greedy(nums.copy())
    print(large_number)
    print(nums)
    large_number = lexicographical_large_number(nums)
    print(large_number)


if __name__ == "__main__":
    main()
