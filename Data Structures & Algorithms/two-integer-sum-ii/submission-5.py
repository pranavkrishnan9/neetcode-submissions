class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1
        left_nums = {}
        right_nums ={}
        #min constraint on numbers input len = 2, always one valid solution
        while left < len(numbers):
            left_nums[numbers[left]] = left
            right_nums[numbers[right]] = right
            if (target - numbers[left] in left_nums) and (left_nums[numbers[left]] != left_nums[target - numbers[left]]):
                return [left_nums[target - numbers[left]] + 1, left_nums[numbers[left]] + 1]
            if (target - numbers[left] in right_nums) and (left_nums[numbers[left]] != right_nums[target - numbers[left]]):
                return [left_nums[numbers[left]] + 1, right_nums[target - numbers[left]] + 1]
            if (target - numbers[right] in left_nums) and (left_nums[target - numbers[right]] != right_nums[numbers[right]]):
                return [left_nums[target - numbers[right]] + 1, right_nums[numbers[right]] + 1]
            if (target - numbers[right] in right_nums) and (right_nums[numbers[right]] != right_nums[target - numbers[right]]):
                return [right_nums[numbers[right]] + 1, right_nums[target - numbers[right]] + 1]
            left += 1
            right -= 1