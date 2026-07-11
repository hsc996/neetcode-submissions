class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # area = height x width
        # height is provided, width = diff of heights[i] + heights[j] (min of both)
        # update max value with each iteration
        l, r = 0, len(heights) - 1
        res = 0

        while l < r:
            area = (r - l) * min(heights[l], heights[r])
            res = max(res, area)

            if heights[l] <= heights[r]:
                l += 1
            else:
                r -= 1
        return res
