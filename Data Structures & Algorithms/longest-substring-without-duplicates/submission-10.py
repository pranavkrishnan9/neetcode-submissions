class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #input = string s
        #output = length of longest substring of s without duplicate chars
        windowLength = 0
        maxWindowLength = 0
        count = {}
        left = 0
        for right in range(len(s)):
            count[s[right]] = count.get(s[right], 0) + 1

            while left < right and count[s[right]] > 1:
                count[s[left]] -= 1
                left += 1
                
            maxWindowLength = max(right - left + 1, maxWindowLength)
        return maxWindowLength
                
            
