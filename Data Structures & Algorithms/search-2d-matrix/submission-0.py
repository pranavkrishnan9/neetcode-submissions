class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #input1: int[] matrix where each row m is sorted in non decreasing order (<=, >= are in play)
        #input2: int target which is the target number we want to find the existence of within matrix
        #output: boolean indicating whether target exists in our matrix

        def target_finder(row):
            left, right = 0, len(row) - 1
            while left <= right:
                mid = (left + right)//2
                if row[mid] < target:
                    left = mid + 1
                elif row[mid] > target:
                    right = mid - 1
                elif row[mid] == target:
                    return True
            return False
        left=0
        right=len(matrix) - 1
        while left <= right:
            mid = (left + right)//2
            row = matrix[mid]
            if target < row[0]:
                right = mid - 1
            elif target > row[-1]:
                left = mid + 1
            else:
                return target_finder(row)
        return False
        

        

        
