class Solution:

    def countPrimes(self, n: int) -> int:
        # isPrime[i] means if i is prime or not
        isPrime = [True] * n
        res = 0

        # 0 and 1 is not prime
        if n <= 1:
            return res

        # Sieve of Eratosthenes
        for i in range(2, n):
            # mark i * i, i * (i + 1), etc to False
            if i * i < n:
                for j in range(i * i, n, i):
                    isPrime[j] = False

        for i in isPrime:
            if i:
                res += 1
        return res - 2  # 0 and 1 is not prime
