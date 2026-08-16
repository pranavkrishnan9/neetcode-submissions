class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s:
            return ""
        count_t = {}
        for c in t:
            count_t[c] = count_t.get(c, 0) + 1

        have = 0
        need = len(count_t)          # number of distinct chars t requires
        count_s = {}
        best = ""
        left = 0

        for right in range(len(s)):
            c = s[right]
            count_s[c] = count_s.get(c, 0) + 1
            if c in count_t and count_s[c] == count_t[c]:
                have += 1                        # this char just became satisfied

            while have == need:                  # O(1) validity check
                currWindow = s[left:right+1]
                if best == "" or len(currWindow) < len(best):
                    best = currWindow
                lc = s[left]
                count_s[lc] -= 1
                if lc in count_t and count_s[lc] < count_t[lc]:
                    have -= 1                     # this char just fell below requirement
                left += 1

        return best