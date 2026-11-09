class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #input = string strs[]
        #output = strs[strs[]] consisting of grouped anagrams
        if len(strs) == 1:
            return [strs]
        anagrams = {}
        for s in strs:
            key = "".join(sorted(s))
            anagrams[key] = anagrams.get(key, []) + [s]

        return list(anagrams.values())
            
            
