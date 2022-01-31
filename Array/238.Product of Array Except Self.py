from typing import List

# Time complexity : O(N) where N represents the number of elements in the input array.
# Space complexity : O(N) used up by the two intermediate arrays
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l_product, r_product = [1] * len(nums), 1
        res = [1] * len(nums)

        # l_product product before i, not including nums[i]
        # no left element before 0, so l_product[0] = 1
        for i in range(1, len(nums)):
            l_product[i] = l_product[i - 1] * nums[i - 1]

        # r_product product after j, not including nums[j]
        # no right element after 0, so r_product[-1] = 1
        for j in range(len(nums) - 1, -1, -1):
            res[j] = r_product * l_product[j]
            r_product *= nums[j]

        return res





# Time complexity : O(N) where N represents the number of elements in the input array.

# Space complexity : O(1) since don't use any additional array for our computations. The problem statement mentions that using the answer array doesn't add to the space complexity.

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)

        res = [1] * n

        # res[i] = product from nums[0] - res[i - 1]
        for i in range(1, n):
            res[i] = res[i - 1] * nums[i - 1]

        # r contains the product of all the elements to the right
        # Note: for the element at index 'length - 1', there are no elements to the right,
        # so the r would be 1
        r = 1

        for i in range(n - 1, -1, -1):
            # r = product from nums[i + 1] - res[n - 1]
            res[i] = r * res[i]
            r *= nums[i]

        return res