class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # sorted, search to find target - ?binary search
        # two pointer approach -> opposite ends, moving in.
        # Add together, if sum < target move l, if sum > target move r
        l, r = 0, len(numbers) - 1

        while l < r:
            tmp = numbers[l] + numbers[r]
            if tmp == target:
                return [l + 1, r + 1]
            elif tmp < target:
                l += 1
            else:
                r -= 1
        return []