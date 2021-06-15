def naive_solution(nums):
    # assume maximum-pairwise-product = 0
    maximum_pairwise_product = 0
    # store total numbers length
    l = len(nums)
    
    # if num is not empty
    if nums:
        for i in range(l):
            for j in range(i + 1, l):
                # if nums[i] * nums[j] > pre_result then modify it
                if maximum_pairwise_product < nums[i] * nums[j]:
                    maximum_pairwise_product = nums[i] * nums[j]
    else:
        # if nums is null return 0
        return 0
    return maximum_pairwise_product

def optimized_solution(nums):
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
        if (nums[j] != nums[max_idx1]) and ((max_idx2 == -1) or nums[j] > nums[max_idx2]):
            max_idx2 = j

    # now return the maximum pairwise product
    return nums[max_idx1] * nums[max_idx2]


def main():
    n = int(input("Enter the value of n: "))
    nums = list(map(int, input().split()))
    # naive solution output
    maximum_pairwise_product = naive_solution(nums)
    print(maximum_pairwise_product)

    # optimized solution output
    maximum_pairwise_product = optimized_solution(nums)
    print(maximum_pairwise_product)

if __name__ == "__main__":
    main()