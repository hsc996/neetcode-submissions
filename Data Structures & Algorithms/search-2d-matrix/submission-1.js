class Solution {
    /**
     * @param {number[][]} matrix
     * @param {number} target
     * @return {boolean}
     */
    searchMatrix(matrix, target) {
        let row_len = matrix[0].length;
        let col_len = matrix.length;

        if (col_len === 0 || row_len === 0) return false;

        let lo = 0;
        let hi = row_len * col_len - 1;

        while (lo <= hi){
            const mid = Math.floor(lo + (hi - lo) / 2);
            const mid_v = matrix[Math.floor(mid / row_len)][mid % row_len];

            if (mid_v === target){
                return true;
            } else if (mid_v < target){
                lo = mid + 1;
            } else {
                hi = mid - 1;
            }
        }

        return false;
    }
}
