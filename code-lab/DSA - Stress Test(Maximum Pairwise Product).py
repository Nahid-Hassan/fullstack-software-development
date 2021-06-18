import random
import heapq

# slow and naive solution


def maximum_pairwise_product(nums):
    maximum_pairwise_product = 0
    if nums:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                prod = nums[i] * nums[j]
                if maximum_pairwise_product < prod:
                    maximum_pairwise_product = prod
    else:
        return 0
    return maximum_pairwise_product


def optimized_solution(nums):
    """
    l = len(nums)

    # find the first maximum/largest number index
    max_idx1 = -1
    for i in range(l):
        # if index 1 greater than index zero than work
        if (max_idx1 == -1) or (nums[i] > nums[max_idx1]):
            max_idx1 = i

    # find the 2nd maximum/largest number index
    max_idx2 = -1
    for j in range(l):
        # (nums[j] != nums[max_idx1]) -> ensure present number is not equal to past number
        if (j != max_idx1) and ((max_idx2 == -1) or nums[j] > nums[max_idx2]):
            max_idx2 = j

    # now return the maximum pairwise product
    return nums[max_idx1] * nums[max_idx2]
    """

    """
    temp = nums.copy()
    max_1 = max(temp)
    temp.remove(max_1)
    max_2 = max(temp)
    return max_1 * max_2
    """

    """
    nums.sort()
    return nums[-1] * nums[-2]
    """
    # heapq.nlargest(n, iterable) return n largest numbers from the
    # iterable.
    a, b = heapq.nlargest(2, nums)
    return a * b


def main():
    while True:
        nums = [random.randint(1, 1000000) for num in range(1000)]

        res1 = maximum_pairwise_product(nums)
        res2 = optimized_solution(nums)

        print(nums)
        print(res1, res2)

        if res1 != res2:
            print(f"Wrong Answer, res1 = {res1} and res2 = {res2}")
            break
        else:
            print("Ok")


if __name__ == "__main__":
    main()
