class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        #input = int(nums) of length n, with range [0, n], no dupes, one number missing
        #output = the missing number from the range

        nums = sorted(nums)
        count = 0
        for n in nums:
            if n != count:
                return count
            count += 1
        return count