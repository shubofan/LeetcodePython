class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []
        for i in range(len(s)):
            if stack and s[i] == stack[-1]:
                stack.pop()
            else:
                stack += s[i]
        return ''.join(stack)
