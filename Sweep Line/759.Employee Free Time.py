from heapq import *
'''
 Time Complexity: O(ClogN), where N is the number of employees, and C is the number of jobs across all employees. 
 The maximum size of the heap is N, so each push and pop operation is O(logN), and there are C such operations.

Space Complexity: O(N)
in additional space complexity. 

'''
# Definition for an Interval.
class Interval(object):
    def __init__(self, start=None, end=None):
        self.start = start
        self.end = end



class Solution(object):
    def employeeFreeTime(self, schedule):
        """
        :type schedule: [[Interval]]
        :rtype: [Interval]
        """
        # build a minheap [(start time, employee id, interval id for an employee)]
        minheap = []
        for emp_id, employee_interval in enumerate(schedule):
            heappush(minheap, (employee_interval[0].start, emp_id, 0)) # just put 1st interval for a employee

        curr_end = schedule[minheap[0][1]][0].end

        ans = []
        while minheap:
            curr_start, emp_id, interval_id = heappop(minheap)
            if curr_start > curr_end: # no overlap
                ans.append(Interval(curr_end, curr_start)) # create a free time interval

            curr_end = max(curr_end, schedule[emp_id][interval_id].end) # adjust the current end time we are tracking
            if interval_id + 1 < len(schedule[emp_id]):
                next_start = schedule[emp_id][interval_id + 1].start
                heappush(minheap, (next_start, emp_id, interval_id + 1))
        return ans


"""
Definition of Interval.
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

# Time complexity: O(nlogn)
#
# Space complexity: O(n)
class Solution:
    """
    @param schedule: a list schedule of employees
    @return: Return a list of finite intervals
    """

    def employeeFreeTime(self, schedule):
        working = []
        for s in schedule:
            for i in range(0, len(s), 2):
                working += [[s[i], s[i + 1]]]

        working.sort()

        res = []

        start, end = working[0][0], working[0][1]
        for i in range(1, len(working)):
            cur = working[i]
            # there is no intersection [start, end], [cur[0], cur[1]], so Interval(end, cur[0]) is free time
            if cur[0] > end:
                res.append(Interval(end, cur[0]))
                start = cur[0]
                end = cur[1]
            else: # intersection exists, merge
                start = min(start, cur[0])
                end = max(end, cur[1])
        return res