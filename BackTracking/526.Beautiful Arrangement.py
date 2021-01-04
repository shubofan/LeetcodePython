class Solution:
    def countArrangement(self, n: int) -> int:
        # if certain number has been used or not in [0 n]
        visited = [0] * (n + 1)
        self.res = 0
        self.dfs(1, visited)
        return self.res

    def dfs(self, pos: int, visited: List[int]):
        # All the numbers has been assigned
        if pos > (len(visited) - 1):
            self.res += 1
        # assign num i to the
        for i in range(1, len(visited)):
            if not visited[i] and (pos % i == 0 or i % pos == 0):
                visited[i] = 1
                self.dfs(pos + 1, visited)
                visited[i] = 0

# class Solution:
#     def countArrangement(self, n: int) -> int:
#         self.res = []
#         nums = [i for i in range(1, n + 1)]
#         self.dfs(nums, [])
#         return len(self.res)

#     def dfs(self, nums: List[int], path: List[int]):
#         if len(nums) == len(path):
#             self.res += [path]
#             return
#         for i in range(len(nums)):
#             if nums[i] not in path and (nums[i] % (len(path) + 1) == 0 or (len(path) + 1) % nums[i] == 0):
#                 self.dfs(nums, path + [nums[i]])
