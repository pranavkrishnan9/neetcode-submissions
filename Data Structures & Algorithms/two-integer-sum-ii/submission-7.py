class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        #inputs: int numbers[] - sorted, non decreasing order, int target
        #output = [i,j] - indices of the two nums in numbers that = target, i < j, i != j
        left = 0
        right = len(numbers) - 1
        while left < right:
            if numbers[left] + numbers[right] < target:
                left += 1
            elif numbers[left] + numbers[right] > target:
                right -= 1
            else:
                return [left + 1, right + 1]