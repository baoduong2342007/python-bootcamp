"""W1-4: Sieve of Eratosthenes translated from C++ to Python.
Difference between C++ and Python:
In C++, the sieve is typically implemented using a fixed-size array or `std::vector<bool>`,
which optimizes storage to 1 bit per element and manages memory statically.
In Python, we allocate a dynamic list `[True] * (n + 1)` where each boolean is a full object,
and we can collect results dynamically using list comprehension without manual sizing.
"""

import math


def primes_up_to(k):
    ans = []
    if k < 2:
        return ans
    nt = [True] * (k + 1)
    nt[0] = nt[1] = False
    for i in range(2, math.isqrt(k) + 1, 1):
        if nt[i]:
            for j in range(i * i, k + 1, i):
                nt[j] = False
    for i in range(2, k + 1):
        if nt[i] == True:
            ans.append(i)
    return ans
