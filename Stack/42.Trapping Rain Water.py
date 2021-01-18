from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        stack = []
        res = 0
        for i in range(n):
            # monotone decreasing stack
            while stack and height[stack[-1]] < height[i]:
                h = height[stack.pop()]
                if not stack:
                    break
                # height[stack[-1]] height of left side, height[i] height of right side
                min_height = min(height[stack[-1]], height[i])
                res += ((i - stack[-1] - 1) * (min_height - h))
            stack += [i]
        return res