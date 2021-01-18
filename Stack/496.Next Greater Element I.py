class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []

        # for num in nums1:
        #     idx = nums2.index(num)
        #     next_ele = -1
        #     for i in range(idx + 1, len(nums2)):
        #         if nums2[i] > num:
        #             next_ele = nums2[i]
        #             break
        #     res += [next_ele]
        # return res

        # key is element in nums2 and value is next greater value for key
        dic1 = {}

        # monotone decreasing stack
        stack = []
        for num in nums2:
            while stack and stack[-1] < num:
                dic1[stack.pop()] = num
            stack += [num]

        for num in nums1:
            res += [dic1.get(num, -1)]
        return res
