class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        num_of_zero = 0
        ele_from_copy = 0

        while ele_from_copy + num_of_zero < len(arr):
            if arr[ele_from_copy] == 0:
                num_of_zero += 1
            ele_from_copy += 1

        lst = len(arr) - 1
        ele_from_copy -= 1

        # Edge case: This zero can't be duplicated. We have no more space,  as left is pointing to the last element
        # which could be included
        # ele_from_copy + 1 = origin size ele_from_copy + num_of_zero + 1 = new array size,
        # if new array size > arr size, just copy last ele_from_copy one time
        if ele_from_copy + num_of_zero + 1 > len(arr):
            arr[lst] = arr[ele_from_copy]
            lst -= 1
            ele_from_copy -= 1
            num_of_zero -= 1

        while num_of_zero > 0:
            if arr[ele_from_copy] == 0:
                arr[lst] = 0
                lst -= 1
                arr[lst] = 0
                num_of_zero -= 1
            else:
                arr[lst] = arr[ele_from_copy]
            lst -= 1
            ele_from_copy -= 1