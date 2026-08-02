class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if len(s) == 0:
            return 0
        left = 0
        windowLength = 0
        maxLength = 0
        count = {}
        maxCount = 0
        for right in range(len(s)):
            count[s[right]] = count.get(s[right], 0) + 1

            maxCount = max(maxCount, count[s[right]])
            windowLength = right - left + 1

            if windowLength - maxCount > k:
                windowLength -= 1
                count[s[left]] -= 1
                left += 1

            maxLength = max(maxLength, windowLength)
        return maxLength
    


