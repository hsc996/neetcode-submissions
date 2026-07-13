class Solution {
    /**
     * @param {number[]} nums
     * @param {number} target
     * @return {number}
     */
    search(nums, target) {
        let lo = 0;
        let hi = nums.length - 1;

        do {
            const m = Math.floor((lo + hi) / 2);
            const v = nums[m];

            if (v === target) {
                return m;
            } else if (v > target) {
                hi = m - 1;
            } else {
                lo = m + 1;
            }
        } while (lo <= hi)
        return -1
    }
}
