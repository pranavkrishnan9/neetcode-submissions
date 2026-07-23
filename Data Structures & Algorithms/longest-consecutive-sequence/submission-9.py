class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        count = 1
        maxCount = 1
        currnum = 0
        nums1 = set(nums)
        for val in nums1:
            if val+1 not in nums1:
                while val - 1 in nums1:
                    count+=1
                    if count > maxCount:
                        maxCount = count
                    val -= 1
                count = 1
        return maxCount

            