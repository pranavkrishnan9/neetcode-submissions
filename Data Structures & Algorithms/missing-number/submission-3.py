class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        #input = int nums[] containing n integers in the range [0, n] no duplicates
        #output = int x, where x is the missing number from the range
        n = len(nums) + 1
        for i in range(n):
            if i not in nums:
                return i