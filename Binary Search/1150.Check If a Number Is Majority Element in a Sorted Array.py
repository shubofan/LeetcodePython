"""
Description

Given an array nums sorted in non-decreasing order, and a number target, return True if and only if target is a majority element.

A majority element is an element that appears more than N/2 times in an array of length N.

"""
from typing import List


class Solution:
    """
    Use binary Search, find the first and last occurrences of A. Then just calculate the difference between the indexes of these occurrences.
    """

    def isMajorityElement(self, nums: List[int], target: int) -> bool:
        n = len(nums)
        l, r = 0, n - 1


        # find 1st occurrence of target
        while l < r:
            mid = (l + l) // 2
            if nums[mid] >= target:
                r = mid
            else:
                l = mid + 1

        l_target = l #  1st occurrence of target
        l, r = 0 , n - 1

        # find last occurrence of target
        while l < r:
            mid = (l + l + 1) // 2
            if nums[mid] <= target:
                l = mid
            else:
                r = mid - 1

        r_target = l # last occurrence of target

        return (r_target - l_target + 1) > n // 2
