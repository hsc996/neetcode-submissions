class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k %= n
        while k:
            tmp = nums[n - 1] #value to insert at front
            for i in range(n -1, 0, -1):
                nums[i] = nums[i - 1] #shift right
            nums[0] = tmp
            k -= 1