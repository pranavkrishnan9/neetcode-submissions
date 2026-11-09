class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #inputs: string s, string t
        #output: bool val indicating if the two strings are anagrams of each other

        #order doesn't mater, counts required (hashmap)
        if len(s) != len(t):
            return False
        count_t = {}
        count_s = {}
        for i in range(len(s)):
            count_t[t[i]] = count_t.get(t[i], 0) + 1
            count_s[s[i]] = count_s.get(s[i], 0) + 1
        return count_t == count_s

            