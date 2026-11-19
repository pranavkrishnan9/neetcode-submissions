class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        #input=int[] nums where every integer appears twice except one int
        #output = integer that appears once
        #thought process: use xor for each number in our nums array
        if len(nums) == 1:
            return nums[0]
        res = nums[0]
        for i in range(1, len(nums)):
            res ^= nums[i]
        return res