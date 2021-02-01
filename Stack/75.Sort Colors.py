class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # all in [0, p0] = 0
        # all in (p0, i) = 1
        # all in (p2, len - 1] = 2

        p0, p2 = 0, len(nums) - 1
        i = 0
        while i <= p2:
            if nums[i] == 0:
                nums[i], nums[p0] = nums[p0], nums[i]
                p0 += 1
                i += 1
            elif nums[i] == 2:
                nums[i], nums[p2] = nums[p2], nums[i]
                p2 -= 1
            elif nums[i] == 1:
                i += 1

#         zero, one, two = 0, 0, 0

#         for i in nums:
#             if i == 0:
#                 zero += 1
#             if i ==1:
#                 one += 1
#             if i ==2:
#                 two += 1
#         i = 0

#         while zero > 0:
#             nums[i] = 0
#             i += 1
#             zero -= 1

#         while one > 0:
#             nums[i] = 1
#             i += 1
#             one -= 1

#         while two > 0:
#             nums[i] = 2
#             i += 1
#             two -= 1





