class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        #inputs: string s, int k
        #take up to k chars of s and replace them with any other char
        #after k replacements, return the length of longest substring with one char in sequence
        count = {}
        left = 0
        maxWindowLength = 0
        maxCount = 0
        for right in range(len(s)):
            windowLength = right - left + 1
            count[s[right]] = count.get(s[right], 0) + 1
            maxCount = max(maxCount, count[s[right]])
            if windowLength - maxCount > k:
                count[s[left]] -= 1
                left += 1
            windowLength = right - left + 1
            maxWindowLength = max(maxWindowLength, windowLength)
        return maxWindowLength




    


