class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        #input = int(nums) of length n, with range [0, n], no dupes, one number missing
        #output = the missing number from the range
        res = len(nums) #our loop will go from 0 to n-1, so include edge case of last num in range
        for i in range(len(nums)):
            res ^= i ^ nums[i]
        return res