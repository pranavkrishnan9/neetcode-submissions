class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #input = int nums[] initially sorted in ascending order rotated between 1 and n times
        #output = index of target number
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right)//2
            if target == nums[mid]:
                return mid
            #one half of a rotated sorted array is always sorted
            #if the first number of our left half is less than the middle number, our left half is sorted
            if nums[left] <= nums[mid]:
                #check if target is in sorted half, mid index already checked so skip
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    #target is in right half
                    left = mid + 1
            #right half is sorted
            elif nums[mid] <= nums[right]:
                #target in right half
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        return -1
