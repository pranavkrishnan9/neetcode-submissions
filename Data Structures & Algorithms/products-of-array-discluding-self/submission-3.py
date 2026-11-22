class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #input = int nums[]
        #output = int output[] where output[i] is the product of all the elements of nums except nums[i]

        output = [1] * len(nums)
        product = 1
        for i in range(len(nums)):
            output[i]*=product
            product*=nums[i]
        product = 1
        for j in range(len(nums) - 1, -1, -1):
            output[j]*=product
            product*=nums[j]
        return output