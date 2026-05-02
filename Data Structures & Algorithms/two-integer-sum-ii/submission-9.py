class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # note: sorted list. Which means can use variation of binary search. OR two pointer, starting from opposite ends.

        l, r = 0, len(numbers) - 1

        while l < r:
            curr_sum = numbers[l] + numbers[r]
            if curr_sum == target:
                return [l + 1, r + 1]
            elif curr_sum < target:
                l += 1
            elif curr_sum > target:
                r -= 1