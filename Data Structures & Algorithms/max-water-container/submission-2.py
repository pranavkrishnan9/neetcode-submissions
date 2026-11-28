class Solution:
    def maxArea(self, heights: List[int]) -> int:
        #input = int heights[] where heights[i] represents the height of ith bar
        #output = the maximum area between two heights/bars
        area = 0
        maxArea = 0

        left = 0
        right = len(heights) - 1
        while left < right:
            width = right - left
            height = min(heights[left], heights[right])
            area = width * height
            maxArea = max(area, maxArea)
            if heights[left] < heights[right]:
                left+=1
            elif heights[right] < heights[left]:
                right-=1
            else:
                left+=1
                right-=1
        return maxArea


