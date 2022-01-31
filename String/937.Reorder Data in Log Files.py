from typing import List
import collections, heapq

class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        letter_logs = []
        digit_logs = []
        res = []

        for log in logs:
            files = log.split(' ')
            if files[1].isdigit():
                digit_logs += [log]
            else:
                letter_logs += [log]

        letter_logs.sort(key=lambda log: (log.split(' ')[1:], log.split(' ')[:1]))

        for log in letter_logs:
            res += [log]

        for log in digit_logs:
            res += [log]

        return res

