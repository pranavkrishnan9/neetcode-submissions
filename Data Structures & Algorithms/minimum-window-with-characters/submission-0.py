class Solution:
    def minWindow(self, s: str, t: str) -> str:
        best = ""
        count_t = {}
        count_s = {}

        for c in t:
            count_t[c] = count_t.get(c, 0) + 1

        #contains helper method
        def contains(count_s, count_t):
            for c in count_t:
                if count_s.get(c,0) < count_t[c]:
                    return False
            return True

        left = 0
        for right in range(len(s)):
            count_s[s[right]] = count_s.get(s[right], 0) + 1
            while contains(count_s, count_t):
                currWindow = s[left:right+1]
                if best == "" or len(currWindow) < len(best):
                    best = currWindow
                count_s[s[left]] -= 1
                if count_s[s[left]] == 0:
                    del count_s[s[left]]
                left += 1
        return best

