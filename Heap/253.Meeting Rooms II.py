import heapq
from typing import List

'''
Time Complexity: O(NlogN)

1: sorting of the array that takes O(NlogN).

2. In the worst case, all N meetings will collide with each other. In any case we have N add operations on the heap. In the worst case we will have N extract-min operations as well.
Overall complexity being (NlogN) since extract-min operation on a heap takes O(logN)


Space Complexity: O(N) because we construct the min-heap and that can contain N elements in the worst case as described above in the time complexity section. Hence, the space complexity is O(N). 

'''

class Solution:
	def minMeetingRooms(self, intervals: List[List[int]]) -> int:

		# If there is no meeting to schedule then no room needs to be allocated.
		if not intervals:
			return 0

		# The heap initialization. Add end time of the pq
		pq = []

		# Sort the meetings by start time.
		intervals.sort(key=lambda x: x[0])

		# Add the first meeting.
		heapq.heappush(pq, intervals[0][1])

		# For all the remaining meeting rooms
		for interval in intervals[1:]:

			# Free the room on top of pq. since current meeting 's start time >= end time of meeting on the top
			if pq[0] <= interval[0]:
				heapq.heappop(pq)

			# If a new room is to be assigned, then also we add to the heap,
			# If an old room is allocated, then also we have to add to the heap with updated end time.
			heapq.heappush(pq, interval[1])

		# The size of the heap tells us the minimum rooms required for all the meetings.
		return len(pq)