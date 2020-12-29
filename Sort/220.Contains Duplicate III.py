from typing import List


class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        # O(n) solution. bucket sort

        buckets = {}  # size of bucket is t + 1, so the buckets like [0, t], [t + 1, 2t + 1]

        for i in range(len(nums)):
            num_of_bucket = nums[i] // (t + 1)

            # the biggest difference in same bucket is always less than t , so always True
            if num_of_bucket in buckets:
                return True
            # abs of range of difference in adjacent bucket is [1 , 2t + 1], so if a new element will be in adjacent bucket, check if difference <= t
            if num_of_bucket + 1 in buckets and abs(buckets[num_of_bucket + 1] - nums[i]) <= t:
                return True
            if num_of_bucket - 1 in buckets and abs(buckets[num_of_bucket - 1] - nums[i]) <= t:
                return True
            buckets[num_of_bucket] = nums[i]

            # remove invalid bucket since difference of indices have already been greater than k
            if i >= k:
                buckets.pop(nums[i - k] // (t + 1))

        return False
