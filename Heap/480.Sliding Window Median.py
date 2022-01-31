import collections
import heapq
from typing import List


class Heap:
    def __init__(self, name="min"):
        self.arr = []
        self.f = lambda x: x if name=="min" else -x
    def push(self, num):
        heapq.heappush(self.arr, self.f(num))                   # 推入一个
    def pop(self):
        return self.f(heapq.heappop(self.arr))                  # 弹出堆顶
    def top(self):
        return self.f(self.arr[0])
    def empty(self):
        return len(self.arr) == 0

class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        small = [] # 较小数字部分使用大根堆
        big = []   # 较大数字部分使用小根堆
        get_mid = lambda x, y: x[0] if k % 2 else (x[0] + y[0]) / 2
        mp = collections.defaultdict(int)
        for i in range(k):
            heapq.heappush(small, nums[i])
        for i in range(k//2):
            heapq.heappush(big, -heapq.heappop(small))
        ans = [get_mid(small, big)]
        print(small, big)
        for i in range(k, len(nums)):
            balance = 0
            l, r = nums[i-k], nums[i]  # 将被删除的窗口最左元素和将被添加到窗口最右的元素
            mp[l] += 1                 # 左窗口元素记账
            if l <= small[0]:
                balance -= 1           # 较小数字堆需删除一个元素
            else:
                balance += 1           # 较大数字堆需删除一个元素
            if r <= small[0]:
                balance += 1           # 较小数字堆添加一个元素
                heapq.heappush(small, r)
            else:
                balance -= 1           # 较大数字堆添加一个元素
                heapq.heappush(big, -r)
            """
            此时balance取值可能是:
            balance | small | big  | 解释
              0     | -1+1  |      | 较小数字堆删除一个元素添加一个元素，两边还是平衡的
              0     |       | +1-1 | 较大数字堆删除一个元素添加一个元素，两边还是平衡的
             -2     | -1    | -1   | 较小数字堆删除一个元素，较大数字堆添加一个元素，失衡
              2     | +1    | +1   | 较大数字堆删除一个元素，较小数字堆添加一个元素，失衡
            """
            print(mp)
            print(balance)
            print(small, big)
            # 较小数字堆挪一个给较大数字堆(3,3)->(4,2)->(3,3)或者(4,3)->(5,2)->(4,3)
            if balance == 2:
                heapq.heappush(big, -heapq.heappop(small))
            # 较大数字堆挪一个给较小数字堆(3,3)->(2,4)->(3,3)或者(4,3)->(3,4)->(4,3)
            if balance == -2:
                heapq.heappush(small, -heapq.heappop(big))
            # 重新达到平衡了,该看看堆顶是不是待删除元素了
            while small and mp[small[0]]:
                mp[small[0]] -= 1
                heapq.heappop(small)
            while  big and mp[-big[0]]:
                mp[-big[0]] -= 1
                heapq.heappop(big)
            # 为什么删除堆顶元素后不用重新平衡两边堆了呢？
            ans.append(get_mid(small, big))
        return ans



class Heap:
    def __init__(self, name="min"):
        self.arr = []
        self.f = lambda x: x if name=="min" else -x
    def push(self, num):
        heapq.heappush(self.arr, self.f(num))                   # 推入一个
    def pop(self):
        return self.f(heapq.heappop(self.arr))                  # 弹出堆顶
    def top(self):
        return self.f(self.arr[0])
    def empty(self):
        return len(self.arr) == 0

class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        small = Heap(name="max") # 较小数字部分使用大根堆
        big = Heap(name="min")   # 较大数字部分使用小根堆
        get_mid = lambda x, y: x.top() if k % 2 else (x.top() + y.top()) / 2
        mp = collections.defaultdict(int)
        for i in range(k):
            small.push(nums[i])
        for i in range(k//2):
            big.push(small.pop())
        ans = [get_mid(small, big)]
        print(small.arr, big.arr)
        for i in range(k, len(nums)):
            balance = 0
            l, r = nums[i-k], nums[i]  # 将被删除的窗口最左元素和将被添加到窗口最右的元素
            mp[l] += 1                 # 左窗口元素记账
            if l <= small.top():
                balance -= 1           # 较小数字堆需删除一个元素
            else:
                balance += 1           # 较大数字堆需删除一个元素
            if r <= small.top():
                balance += 1           # 较小数字堆添加一个元素
                small.push(r)
            else:
                balance -= 1           # 较大数字堆添加一个元素
                big.push(r)
            """
            此时balance取值可能是:
            balance | small | big  | 解释
              0     | -1+1  |      | 较小数字堆删除一个元素添加一个元素，两边还是平衡的
              0     |       | +1-1 | 较大数字堆删除一个元素添加一个元素，两边还是平衡的
             -2     | -1    | -1   | 较小数字堆删除一个元素，较大数字堆添加一个元素，失衡
              2     | +1    | +1   | 较大数字堆删除一个元素，较小数字堆添加一个元素，失衡
            """
            print(mp)
            print(balance)
            print(small.arr, big.arr)
            # 较小数字堆挪一个给较大数字堆(3,3)->(4,2)->(3,3)或者(4,3)->(5,2)->(4,3)
            if balance == 2:
                big.push(small.pop())
            # 较大数字堆挪一个给较小数字堆(3,3)->(2,4)->(3,3)或者(4,3)->(3,4)->(4,3)
            if balance == -2:
                small.push(big.pop())
            # 重新达到平衡了,该看看堆顶是不是待删除元素了
            while not small.empty() and mp[small.top()]:
                mp[small.top()] -= 1
                small.pop()
            while not big.empty() and mp[big.top()]:
                mp[big.top()] -= 1
                big.pop()
            # 为什么删除堆顶元素后不用重新平衡两边堆了呢？
            ans.append(get_mid(small, big))
        return ans

