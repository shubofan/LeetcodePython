from typing import List

"""
Time complexity: O(n).Each bar can be touched at most twice(due to insertion and deletion from stack) 
and insertion and deletion from stack takes O(1) time. 

Space complexity: O(n) Stack can take upto O(n) space in case of stairs-like or flat structure. 
"""
class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        stack = []
        res = 0
        for i in range(n):
            # monotone decreasing stack of height,but put index to the stack, so height[stack[-1]] is min height
            while stack and height[stack[-1]] < height[i]:
                h = height[stack.pop()]
                if not stack: #  not left boundary, so cannot store water
                    break
                # bounded height: height[stack[-1]] height of left side, height[i] height of right side
                bounded_height = min(height[stack[-1]], height[i])
                res += ((i - stack[-1] - 1) * (bounded_height - h))
            stack += [i]
        return res


class Solution:
    def trap(self, height: List[int]) -> int:
        ans = 0
        left, right = 0, len(height) - 1
        leftMax = rightMax = 0

        while left < right:
            leftMax = max(leftMax, height[left])
            rightMax = max(rightMax, height[right])
            # right is the higher wall
            if height[left] < height[right]:
                ans += leftMax - height[left]
                left += 1
            else:
                ans += rightMax - height[right]
                right -= 1

        return ans
