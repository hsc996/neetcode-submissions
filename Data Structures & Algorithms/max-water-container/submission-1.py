class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # Find greatest area -> req. finding greatest heights
        # Use two pointer approach, starting at opposite ends and moving in 
        # Calculate the area and update max area for each iteration
        # Move whichever pointer is pointing at the lesser value

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