class Solution:
    def trap(self, height: List[int]) -> int:
        total = 0
        while sum(height) > 0:
            level = [int(h > 0) for h in height]
            total += self.count_water_holes(level)

            height = [max(0, h - 1) for h in height]

        return total

    def count_water_holes(self, arr):
        arr = arr[arr.index(1):]
        arr.reverse()
        arr = arr[arr.index(1):]

        return len(arr) - sum(arr)
