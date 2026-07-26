class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sortedNums = sorted(nums)
        result = []
        # 0 - currSum = sortedNums[k]
        for i in range(len(sortedNums)):
            if i > 0 and sortedNums[i] == sortedNums[i-1]:
                continue
            left = i + 1
            right = len(nums) - 1
            target = -sortedNums[i]
            while left < right:
                if sortedNums[left] + sortedNums[right] == target:
                   result.append([sortedNums[left], sortedNums[i], sortedNums[right]])
                   #can't use these indices again for the same loop so skip both
                   left += 1
                   right -= 1
                   while left < right and sortedNums[left] == sortedNums[left-1]:
                        left += 1
                   while left < right and sortedNums[right] == sortedNums[right+1]:
                        right -= 1
                elif sortedNums[left] + sortedNums[right] < target:
                    left += 1
                else:
                    right -= 1
        return result
                
                
