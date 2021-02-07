class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        n = len(nums)
        if n <= 2:
            return True
        cnt = 0
        for i in range(0, n - 1):
            if nums[i] > nums[i + 1]:
                cnt += 1
                if i > 0:
                    if nums[i + 1] >= nums[i - 1]:  # best way to adjust is to decrease nums[i]. since nums[i + 2],
                        # nums[i+3] ....  might > nums[i + 1] but <= nums[i], it is possible to create the Non-decreasing array by decrease nums[i] to nums[i - 1]
                        nums[i] = nums[i - 1]
                    else:
                        #  At this time nums[i + 1] < nums[i] and nums[i + 1] < nums[i - 1], cannot decrease nums[i]
                        #  to = nums[i - 1], because if so, both nums[i] == nums[i - 1] and nums[i+1] < nums[i - 1],
                        #  the array is still not valid. hence,  only way to adjust it make nums[i + 1] = nums[i]
                        nums[i + 1] = nums[i]
                if cnt == 2:
                    return False
        return True
