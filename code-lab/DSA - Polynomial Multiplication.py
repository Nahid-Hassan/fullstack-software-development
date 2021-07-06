n = 3
a = (3, 2, 5)
b = (5, 1, 2)

c = [15, 13, 33, 9, 10]


def polynomial_multiplication_naive(a, b, n):
    product = [0] * (2*n - 1)
    # print(product)

    for i in range(n):
        for j in range(n):
            product[i+j] = product[i+j] + a[i] * b[j]

    return product


# def polynomial_multiplication_div_and_conquer(a, b, n, a1, b1):
#     product = [0] * (2*n - 1)
#     if n == 1:
#         product[0] = a[a1] * b[b1]
#         return product
#     product[:n-2] = polynomial_multiplication_div_and_conquer(a, b, n/2, a1, b1)
#     product[n:] = polynomial_multiplication_div_and_conquer(a, b, n/2, a1 + n/2, b1 + n/2)



def main():
    out = polynomial_multiplication_naive(a, b, n)
    print(out)
    assert out == c, 'Output not matched!'


if __name__ == "__main__":
    main()
