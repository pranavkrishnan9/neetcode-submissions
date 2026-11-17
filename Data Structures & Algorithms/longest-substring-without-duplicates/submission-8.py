from collections import defaultdict
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #input = string s
        #output = int length where length represents the longest substring of s without duplicate chars
        seen = {}
        left = 0
        right = 0
        maxWindowLength = 0

        while right < len(s):
            curr_char = s[right]
            seen[curr_char] = seen.get(curr_char, 0) + 1
            while seen[curr_char] > 1:
                seen[s[left]] -= 1
                left += 1
            currWindowLength = right - left + 1
            maxWindowLength = max(currWindowLength, maxWindowLength)
            right += 1
        return maxWindowLength