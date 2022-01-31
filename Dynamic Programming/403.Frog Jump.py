from typing import List


class Solution:
	# map ，其中key=stone, value={from previous stone 可以到达stone的跳跃步长组成的集合 }。那么能够到达stone等价于dp[stone]非空。
	def canCross(self, stones: List[int]) -> bool:

		dic = {}
		for stone in stones:
			dic[stone] = set()
		dic[stones[0]].add(0)  # for 1st stone, take 0 step to it

		for i, stone in enumerate(stones):
			for k in dic[stone]:  # all possible k that lead to current stone
				for step in range(k - 1, k + 2):  # all possible steps [k-1, k+1]
					if step > 0 and (stone + step) in dic:  # if we can take step from current stone to next possible stone, update next stone with corrsponding step
						dic[stone + step].add(step)  # current stone(stone) take step -> next stone (stone + step)

		return len(dic[stones[-1]]) > 0  # last stone is reachable