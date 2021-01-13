class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        n = len(nums)

        if n == 1:
            return True if nums[0] == target else False

        l, r = 0, n - 1
        while l <= r:
            m = (l + r) // 2

            if nums[m] == target:
                return True
            if nums[m] == nums[l]:
                l += 1
            elif nums[m] < nums[l]:
                # right is ordered
                if nums[m] < target <= nums[r]:
                    l = m + 1
                else:
                    r = m - 1
            else:
                # left is ordered
                if nums[l] <= target < nums[m]:
                    r = m - 1
                else:
                    l = m + 1
        return False
