class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        # track remaining weight allocation by subtracting each w from limit
        people.sort()
        res = 0
        l, r = 0, len(people) - 1
        while l <= r:
            remainder = limit - people[r]
            r -= 1
            res += 1
            if l <= r and remainder >= people[l]:
                l += 1
        return res
