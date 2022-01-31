from typing import List


class Solution:
    #Time O(N^2), work like the bubble sort. Each iteration place 1 element to the right place
    #Space O(N), res may take O(N)
    def pancakeSort(self, arr: List[int]) -> List[int]:
        res = []
        n = len(arr)
        # element to be placed from n to 1
        element_to_place = n
        while element_to_place > 0:
            i = arr.index(element_to_place)
            # [3, 2,4,1] -> [4,2,3,1]
            if element_to_place != arr[i - 1]:
                res += [i + 1]
                arr[:i+1] = arr[:i+1][::-1] # Place the element_to_place to the first
                # [4,2,3,1] -> [1,3,2,4] where 4 is in the correct place, next step, try place 3
                if arr[element_to_place-1] != element_to_place:
                    res += [element_to_place]
                    arr[:element_to_place] = arr[:element_to_place][::-1]
            element_to_place -= 1
        return res
