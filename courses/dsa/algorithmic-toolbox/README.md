# Algorithmic Toolbox

## Table of Contents

- [Algorithmic Toolbox](#algorithmic-toolbox)
  - [Table of Contents](#table-of-contents)
    - [Programming Challenges](#programming-challenges)
      - [Prerequisites](#prerequisites)
      - [Sum of Two Digits](#sum-of-two-digits)
      - [Maximum Pairwise Product](#maximum-pairwise-product)

### Programming Challenges

#### Prerequisites

- Programming Languages(Python, Java, C++) - Any of them.
- [Discrete Mathematics](https://www.coursera.org/learn/what-is-a-proof?specialization=discrete-mathematics)

#### Sum of Two Digits

```py
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
```

#### Maximum Pairwise Product

- **Naive Solution**:

```py
def naive_solution(nums):
    # assume maximum-pairwise-product = 0
    maximum_pairwise_product = 0
    # store total numbers length
    l = len(nums)

    # if num is not empty
    if nums:
        for i in range(l):
            for j in range(i + 1, l):
                if maximum_pairwise_product < nums[i] * nums[j]:
                    maximum_pairwise_product = nums[i] * nums[j]
    else:
        return 0
    return maximum_pairwise_product

def main():
    nums = list(map(int, input().split()))
    maximum_pairwise_product = naive_solution(nums)
    print(maximum_pairwise_product)

if __name__ == "__main__":
    main()
```

But above solution isn't correct. It occur a `Time Limit Error` error. So we need to optimize it.

One optimization is first find the `two maximum numbers` from the array, then return the multiplication of this two numbers.

```py
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
```
