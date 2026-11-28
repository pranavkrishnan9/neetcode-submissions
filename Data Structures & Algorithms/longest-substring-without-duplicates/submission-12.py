class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #input = string s
        #output = length of the longest substring of s without duplicate chars
        #sliding window problem
        left = 0
        windowLength = 0
        maxWindowLength = 0
        count = {}
        for right in range(len(s)):
            count[s[right]] = count.get(s[right], 0) + 1
            
            while count[s[right]] > 1:
                count[s[left]] -= 1
                left += 1
                
            windowLength = right - left + 1
            maxWindowLength = max(windowLength, maxWindowLength)
        return maxWindowLength