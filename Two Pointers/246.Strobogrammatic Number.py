class Solution:
    """
    @param num: a string
    @return: true if a number is strobogrammatic or false
    """
    def isStrobogrammatic(self, nums):
        d = {'0':'0','1':'1', '8':'8', '6':'9', '9':'6'}

        l, r = 0, len(nums) - 1

        while l <= r:
            if nums[l] not in d or nums[r] not in d:
                return False
            if d[nums[l]] != nums[r] or d[nums[r]] != nums[l]:
                return False
            l += 1
            r -= 1
        return True
