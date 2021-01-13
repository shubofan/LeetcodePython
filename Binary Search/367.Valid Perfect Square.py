class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if 0 < num < 2:
            return True
        l = 2
        r = num
        while l < r:
            mid = (l + r) // 2
            if mid * mid < num:
                l = mid + 1
            else:
                r = mid
        return l * l == num