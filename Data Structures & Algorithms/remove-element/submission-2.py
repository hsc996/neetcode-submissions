class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        tmp = []

        for n in nums:
            if val == n:
                continue
            tmp.append(n)
        for i in range(len(tmp)):
            nums[i] = tmp[i]
        return len(tmp)