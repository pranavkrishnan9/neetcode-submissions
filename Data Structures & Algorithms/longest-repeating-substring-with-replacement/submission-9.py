class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        #inputs: string s, int k
        #output: int maxWindow, where res is the length of the longest substring with one distinct char after k replacements

        left = 0
        count = {}
        currWindow = 0
        maxWindow = 0
        for right in range(len(s)):
            count[s[right]] = count.get(s[right], 0) + 1

            while (right - left + 1) - max(count.values()) > k:
                count[s[left]] -= 1
                left += 1
            
            currWindow = right - left + 1
            maxWindow = max(currWindow, maxWindow)
        return maxWindow