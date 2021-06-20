import time
import math
import random

def gcd_naive(a, b):
    mx = max(a, b)

    gcd = 1
    for i in range(2, mx):
        if a % i == 0 and b % i == 0:
            gcd = i
    return gcd


def gcd_naive_2(a, b):
    gcd = 1
    for i in range(2, max(a, b) // 2):
        if a % i == 0 and a % b == 0:
            gcd = i
    return gcd


def gcd_naive_3(a, b):
    gcd = 1
    for i in range(2, math.ceil(math.sqrt(max(a, b)))):
        if a % i == 0 and a % b == 0:
            gcd = i
    return gcd

def main():

    for i in range(10):
        a = random.randint(1,10000)
        b = random.randint(1,10000)
        start_time = time.time()
        gcd_naive(a, b)
        print("--- %s seconds 1---" % (time.time() - start_time))

        start_time = time.time()
        gcd_naive_2(a, b)
        print("--- %s seconds 2---" % (time.time() - start_time))

        start_time = time.time()
        gcd_naive_3(a, b)
        print("--- %s seconds 3---" % (time.time() - start_time))

        print("-------------------------------------------------")
if __name__ == "__main__":
    main()
