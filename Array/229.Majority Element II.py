from typing import List


class Solution:
    # Boyer-Moore Majority Vote algorithm
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        # At most 2 numbers which appear more the n / 3 times in the array
        # Assign first element to both candidate1 and candidate2
        cand1, cand2 = nums[0], nums[0]
        cnt1, cnt2 = 0, 0

        for num in nums:
            if num == cand1:
                cnt1 += 1
            elif num == cand2:
                cnt2 += 1
            # replace candidate1
            elif cnt1 == 0:
                cand1 = num
                cnt1 += 1
            elif cnt2 == 0:
                cand2 = num
                cnt2 += 1
            else:
                cnt1 -= 1
                cnt2 -= 1

        cnt1, cnt2 = 0, 0

        # recount the candidate
        for num in nums:
            if num == cand1:
                cnt1 += 1
            elif num == cand2:
                cnt2 += 1
                # return based on the real count of each candidate
        if cnt1 > n // 3 and cnt2 > n // 3:
            return [cand1, cand2]
        elif cnt1 > n // 3:
            return [cand1]
        elif cnt2 > n // 3:
            return [cand2]
        else:
            return []
