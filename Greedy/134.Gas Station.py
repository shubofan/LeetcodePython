from typing import List


class ListNode:
    def __init__(self, val: int, pre=None, next=None):
        """
        Initialize your data structure here.
        """
        self.val = val
        self.pre = pre
        self.next = next


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if not gas or not cost:
            return -1
        n = len(gas)
        for i in range(n):
            if cost[i] > gas[i]:
                continue
            else:
                tank = gas[i]
                start = i
                while tank > 0:
                    # try to move forward
                    start = (start + 1) % n
                    # consume the cost
                    tank = tank - cost[start - 1]
                    # if after consuming the cost, the tank is < 0, which means next index is not reachable
                    if tank < 0:
                        continue
                    # move forward to fill the fas
                    else:
                        tank += gas[start]

                    if start == i:
                        return i

        return -1
