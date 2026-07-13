class Solution {
    /**
     * @param {number[]} nums
     * @param {number} target
     * @return {number}
     */
    search(nums, target) {
        let lo = 0, hi = nums.length - 1;
        while (lo<=hi){
            let m = Math.floor((lo + hi) / 2);
            if (nums[m] === target)   return m;
            else if (nums[m] > target)    hi = m -1;
            else    lo = m + 1;
        }
        return -1;
    }
}
