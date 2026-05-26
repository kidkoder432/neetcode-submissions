class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, k in enumerate(nums):
            for j, l in enumerate(nums):
                if k + l == target and i != j:
                    return [i, j]
    