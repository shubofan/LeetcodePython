import collections
class Solution:
    """
    @param strings: a string array
    @return: return a list of string array
    """
    def groupStrings(self, strings):
        dic = collections.defaultdict(list)

        for s in strings:
            offset = ''
            for i in range(len(s)-1):
                # offset of abc is (1,1,) offset of bcd is also (1,1,)

                # offset of 'az' is (25,), offset of 'ba' is -1, so need to convert to 25
                offset = offset + str((ord(s[i+1]) - ord(s[i]) + 26) % 26) +  ','

            dic[offset] += [s]

        res = [v for v in dic.values()]
        return res