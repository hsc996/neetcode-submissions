class Solution {
    /**
     * @param {number[]} nums
     * @param {number} target
     * @return {number}
     */
    search(nums, target) {
        let lo = 0;
        let hi = nums.length;

        do {
            const mid = Math.floor(lo + (hi -lo) / 2);
            const val = nums[mid]

            if (val === target){
                return mid;
            } else if (val > target){
                hi = mid;
            } else {
                lo = mid + 1;
            }

        } while (lo < hi)
        return -1
    }
}
