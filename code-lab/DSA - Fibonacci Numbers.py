import random
import math


def fibonacci_recursive(n):
    if n <= 1:
        return n

    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)


def fibonacci_iterative(n):
    fib = [0, 1]
    for i in range(2, n+1):
        fib.append(fib[i-1]+fib[i-2])

    return fib[n]


def fibonacci_formula(n):
    root_5 = math.sqrt(5.0)

    return (1 / root_5) * ((((1 + root_5) / 2) ** n) - (((1 - root_5) / 2) ** n))


def main():
    # stress test
    for _ in range(10):
        n = random.randint(1, 20)

        recursive = fibonacci_recursive(n)
        iterative = fibonacci_iterative(n)
        method = fibonacci_formula(n - 1)

        print(n, '---->', math.floor(method))

        if recursive != iterative:
            print(
                f'Wrong Answer: recursive = {recursive}, iterative = {iterative}.')
        else:
            print('Ok')


if __name__ == "__main__":
    main()
