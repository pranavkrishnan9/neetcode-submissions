class Solution:
    def trap(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        maxArea = 0
        maxLeft = height[left]
        maxRight = height[right]
        maxArea = 0
        while left < right:
            if height[left] < height[right]:
                maxArea += min(maxLeft, maxRight) - height[left]
                left += 1
                if height[left] > maxLeft:
                    maxLeft = height[left]
                continue
            maxArea += min(maxLeft, maxRight) - height[right]
            right -= 1
            if height[right] > maxRight:
                maxRight = height[right]
        return maxArea