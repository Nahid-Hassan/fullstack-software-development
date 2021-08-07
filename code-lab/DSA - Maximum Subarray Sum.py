import random


def maximum_subarray_sum_slow(nums, n):
    best = 0

    for i in range(n):
        for j in range(i, n):
            sum = 0
            for k in range(i, j+1):
                sum += nums[k]
            best = max(best, sum)
    return best

def maximum_subarray_sum_medium(nums, n):
    best = 0

    for i in range(n):
        sum = 0
        for j in range(i, n):
            sum += nums[j]
            best = max(best, sum)
    return best


def maximum_subarray_sum_fast(nums, n):
    best, sum = 0, 0
    for i in range(n):
        sum = max(nums[i], sum + nums[i])
        best = max(best, sum)
    
    return best


def main():
    nums = [random.randint(-10, 10) for _ in range(10)]
    print(nums)

    res1 = maximum_subarray_sum_slow(nums, len(nums))
    res2 = maximum_subarray_sum_medium(nums, len(nums))
    res3 = maximum_subarray_sum_fast(nums, len(nums))

    assert(res1, res2)
    assert(res2, res3)

if __name__ == "__main__":
    main()
