from collections import defaultdict
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        seen = set()
        maxWindow = 1
        currWindow = 1
        left = 0
        right = 0
        while right < len(s):
            if s[right] in seen:
                if len(s[left:right]) > maxWindow:
                    maxWindow = len(s[left:right])
                while s[right] in seen:
                    seen.remove(s[left])
                    left += 1
            seen.add(s[right])
            right += 1
            if len(s[left:right]) > maxWindow:
                maxWindow = len(s[left:right])
        return maxWindow
            