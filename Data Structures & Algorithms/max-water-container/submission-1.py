class Solution:
    def maxArea(self, heights: List[int]) -> int:
        #input = int heights[], where heights[i] represents the height of the ith bar
        #output = int maxArea, where maxArea represents the max area between two heights in heights[]
        left = 0 
        right = len(heights) - 1

        maxArea = 0
        while left < right:
            minHeight = min(heights[left], heights[right])
            area = minHeight * (right - left)
            if area > maxArea:
                maxArea = area
            if heights[left] < heights[right]:
                left += 1
            elif heights[right] < heights[left]:
                right -= 1
            else:
                left += 1
                right -= 1
        return maxArea


