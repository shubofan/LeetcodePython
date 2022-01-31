import collections


class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        #         if n == 1:
        #             return 1
        #         leave = [False] * n
        #         next_i = 0
        #         eliminated = 0

        #         while True:
        #             # print(leave)
        #             cnt = 0
        #             l = next_i
        #             while True:
        #                 l %= (n)
        #                 if not leave[l]:
        #                     cnt += 1
        #                 if cnt == k:
        #                     break
        #                 else:
        #                     l += 1
        #             leave[l] = True # eliminate l
        #             eliminated += 1

        #             while True:
        #                 l %= (n)
        #                 if leave[l]:
        #                     l += 1
        #                 else:
        #                     next_i = l
        #                     break
        #             if n - eliminated == 1:
        #                 return l + 1

        q = collections.deque()
        for i in range(1, n + 1):
            q += [i]

        while len(q) > 1:
            cnt = 0
            while cnt < k:
                q.append(q.popleft())
                cnt += 1
            q.pop()
        return q[0]
