class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        count = 1
        maxcount = 1
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return 1
        nums1 = sorted(nums)
        for i in range(1, len(nums1)):
            if nums1[i-1] == nums1[i]:
                continue
            if nums1[i-1] == nums1[i] - 1:
                count+=1
                if count >= maxcount:
                    maxcount = count
                continue
            count=1
        return maxcount

            