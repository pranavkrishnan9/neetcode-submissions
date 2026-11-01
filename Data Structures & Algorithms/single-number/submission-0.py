class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        xor_arr = 0;
        for i in range(len(nums)):
            xor_arr = xor_arr ^ nums[i]
        return xor_arr;