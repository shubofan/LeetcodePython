class Solution:
    def isHappy(self, n: int) -> bool:
        if n == 1:
            return True
        s = set()

        while n > 1:
            if n in s:
                break
            else:
                s.add(n)
                sum = 0
                while n > 0:
                    sum += (n % 10) ** 2
                    n = n // 10
                n = sum
        return True if n == 1 else False

