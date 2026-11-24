class Solution:
    def trap(self, heights: List[int]) -> int:

        left, right = 0, len(heights) - 1
        left_max, right_max = 0, 0
        total_water = 0

        while left < right:
            left_max = max(left_max, heights[left])
            right_max = max(right_max, heights[right])

            if left_max < right_max:
                total_water += left_max - heights[left]
                left += 1
            else:
                total_water += right_max - heights[right]
                right -= 1

        return total_water