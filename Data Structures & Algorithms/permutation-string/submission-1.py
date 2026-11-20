class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        #inputs: string s1, string s2
        #output: bool val = true if s2 contains permutation of s1, false otherwise
        if len(s1) > len(s2):
            return False
        count_s1 = {}
        count_s2 = {}
        for i in range(len(s1)):
            count_s1[s1[i]] = count_s1.get(s1[i], 0) + 1
            count_s2[s2[i]] = count_s2.get(s2[i], 0) + 1
        if count_s1 == count_s2:
            return True
        left = 0
        right = len(s1)
        while right < len(s2):
            count_s2[s2[right]] = count_s2.get(s2[right], 0) + 1
            count_s2[s2[left]] -= 1
            if count_s2[s2[left]] == 0:
                del count_s2[s2[left]]
            left += 1
            if count_s1 == count_s2:
                return True
            right += 1
        return False


