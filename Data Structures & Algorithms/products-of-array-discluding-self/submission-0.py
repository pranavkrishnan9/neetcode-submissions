class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        output = [1] * len(nums)
        for i in range(len(nums)):
            output[i] = product
            product *= nums[i]
        product = 1
        for j in range(len(nums) - 1, -1, -1):
            output[j] *= product
            product *= nums[j]
        return output
            
            