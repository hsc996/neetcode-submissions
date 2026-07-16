class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # area = height x width (idx)
        l,r = 0, len(heights) - 1
        max_a = 0
        while l < r:
            area = min(heights[l], heights[r]) * (r - l)
            max_a = max(max_a, area)
            if heights[l] <= heights[r]:
                l += 1
            else:
                r -= 1
        return max_a