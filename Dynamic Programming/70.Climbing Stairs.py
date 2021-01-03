class Solution:
    def climbStairs(self, n: int) -> int:

        if n == 1 or n == 2:
            return n

        one_step_before = 1
        two_steps_before = 2
        res = 0

        for i in range(2, n):
            res = one_step_before + two_steps_before
            one_step_before, two_steps_before = two_steps_before, res
        return res
