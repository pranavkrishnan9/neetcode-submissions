class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        #input = int nums[]
        #output = list of unique index triplets [i,j,k] where i != j != k and nums[i] + nums[j] + nums[k] = 0
        output = []
        nums = sorted(nums)
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            left = i+1
            right = len(nums) - 1
            target = -nums[i]
            while left < right:
                if nums[left] + nums[right] < target:
                    left += 1
                elif nums[left] + nums[right] > target:
                    right -= 1
                elif nums[left] + nums[right] == target:
                    output.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1

                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
        return output
                

