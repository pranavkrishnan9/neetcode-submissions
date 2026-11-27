class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #input = string strs[]
        #output = strs[strs[]] consisting of grouped anagrams
        anagrams = {}
        res = []
        if len(strs) == 1:
            return [strs]
        for s in strs:
            s1 = "".join(sorted(s))
            if s1 not in anagrams:
                anagrams[s1] = []
            anagrams[s1].append(s)
        res = list(anagrams.values())
        return res
            
