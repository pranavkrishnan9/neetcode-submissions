class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #input = nums[]
        #output = copy of nums[] altered
        
        #copy all the items with the left product accumulated
        product = 1
        output = [1] * len(nums)
        for i in range(len(nums)):
            output[i] = product
            product *= nums[i]
        #reset product for accumulating right product
        product = 1
        for j in range(len(nums) - 1, -1, -1):
            output[j] *= product
            product *= nums[j]
        return output