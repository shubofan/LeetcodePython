import collections


class Solution(object):
    def isPossible(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        cnt = collections.Counter(nums)
        # key is the last number of a consecutive subsequence, value if number of sequences end with key
        end = collections.defaultdict(int)

        for num in nums:
            if cnt[num] <= 0:
                continue
            # num - 1 is the last element , now just append num to num - 1
            if num - 1 in end and end[num - 1] > 0:
                end[num] += 1
                end[num - 1] -= 1
                cnt[num] -= 1
            # num must be the 1st element of a new consecutive subsequence, so num + 1, num + 2 should exist
            elif cnt[num + 1] > 0 and cnt[num + 2] > 0:
                end[num + 2] += 1
                cnt[num] -= 1
                cnt[num + 1] -= 1
                cnt[num + 2] -= 1
            # cannot form a consecutive subsequence
            else:
                return False
        return True
