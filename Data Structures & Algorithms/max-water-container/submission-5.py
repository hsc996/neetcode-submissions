class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # area = height * width (diff of idx)
        # two pointers, find shortest height
        # move from out to in
        l, r = 0, len(heights) - 1
        res = 0

        while l < r:
            area = min(heights[l], heights[r]) * (r - l)
            res = max(res, area)
            if heights[l] <= heights[r]:
                l += 1
            else:
                r -= 1
        return res