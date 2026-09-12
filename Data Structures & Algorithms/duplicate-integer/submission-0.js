class Solution {
    /**
     * @param {number[]} nums
     * @return {boolean}
     */
    hasDuplicate(nums) {
        const n=new Set(nums)
        console.log(n.size,nums.length)
        return n.size!=nums.length
    }
}
