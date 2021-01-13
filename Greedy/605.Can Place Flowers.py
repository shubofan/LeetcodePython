class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        total = 0
        if not flowerbed:
            return False

        if n == 0:
            return True

        for i in range(len(flowerbed)):
            if flowerbed[i] == 1:
                continue
            elif i > 0 and flowerbed[i - 1] == 1:
                continue
            elif i < len(flowerbed) - 1 and flowerbed[i + 1] == 1:
                continue
            else:
                flowerbed[i] = 1
                n -= 1

        return n <= 0