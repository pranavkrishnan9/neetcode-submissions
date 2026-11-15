class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #inputs: string s, string t
        #output: bool val indicating if the two strings are anagrams of each other

        #order doesn't mater, counts required (hashmap)
        count_s = {}
        count_t = {}

        for c in s:
            count_s[c] = count_s.get(c, 0) + 1
        
        for c in t:
            count_t[c] = count_t.get(c, 0) + 1
        
        if count_s != count_t:
            return False
        return True