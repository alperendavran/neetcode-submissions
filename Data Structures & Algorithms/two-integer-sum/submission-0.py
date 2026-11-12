class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indices = {}

        for idx, num in enumerate(nums):
            indices[num] = idx

        for idx, num in enumerate(nums):
            remaining = target - num

            if remaining in indices and indices[remaining] != idx:
                return [idx, indices[remaining]]