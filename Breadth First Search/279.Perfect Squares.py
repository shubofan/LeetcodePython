import math


class Solution:
    #     def numSquares(self, n: int) -> int:
    #         perfect = [float('inf')] * (n + 1)
    #         perfect[1] = 1
    #         square_nums = [i**2 for i in range(0, int(math.sqrt(n))+1)]

    #         for i in range(1, n + 1):
    #             if i in square_nums:
    #                 perfect[i] = 1
    #             else:
    #                 j = 1
    #                 while j**2 < i:
    #                     perfect[i] = min(perfect[i], 1 + perfect[i - j**2])
    #                     j += 1
    #         return perfect[-1]

    # BFS
    def numSquares(self, n: int) -> int:
        square_nums = [i ** 2 for i in range(0, int(math.sqrt(n)) + 1)]

        # use set to mimic a queue so to ensure no duplicate number
        q = set()
        q.add(n)
        level = 1

        while q:
            nextq = set()
            for element in q:
                for num in square_nums:
                    if num == element:
                        return level
                    elif num < element:
                        nextq.add(element - num)
                    else:
                        break
            level += 1
            q = nextq
        return level

