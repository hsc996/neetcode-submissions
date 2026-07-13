class Solution {
    /**
     * @param {number[]} nums
     * @param {number} target
     * @return {number}
     */
    searchInsert(nums, target) {
        let lo = 0, hi = nums.length;
        while (lo<hi){
            let m = Math.floor(lo + (hi - lo) / 2);
            if (nums[m] === target)  return m;
            else if (nums[m] > target)  hi = m;
            else     lo = m + 1;
        }
        return lo;
    }
}
