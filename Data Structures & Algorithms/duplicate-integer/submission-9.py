class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #input = int nums[]
        #output = bool val indicating whether nums contains a duplicate

        seen = set(nums)
        if len(nums) != len(seen):
            return True
        return False