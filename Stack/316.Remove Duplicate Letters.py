class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        counter = [0] * 26
        for letter in s:
            counter[ord(letter) - 97] += 1

        stack = []

        for letter in s:
            if letter not in stack:
                while stack and letter < stack[-1] and counter[ord(stack[-1]) - 97] > 0:
                    stack.pop()
                stack += [letter]
            counter[ord(letter) - 97] -= 1
        return ''.join(stack)
