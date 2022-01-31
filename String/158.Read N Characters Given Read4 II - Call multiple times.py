"""
The read4 API is already defined for you.
@param buf a list of characters
@return an integer
you can call Reader.read4(buf)
"""


class Solution:

    # @param {char[]} buf destination buffer
    # @param {int} n maximum number of characters to read
    # @return {int} the number of characters read
    def __init__(self):
        self.q = collections.deque()
    def read(self, buf, n):
        idx = 0
        while idx < n:
            if self.q:
                buf[idx] = self.q.popleft()
                idx += 1
            else:
                # buf4 is used for received lists from API call
                buf4 = [''] * 4
                length = Reader.read4(buf4)
                if length == 0:
                    break
                for i in range(length):
                    self.q += buf4[i]
        return idx
