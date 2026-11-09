class Solution {
public:
    bool isAnagram(string s, string t) {
        //inputs: string s, string t
        //output: bool val -> true if s and t are anagrams of each other, false if not

        //anagram = words in which the frequency of chars in string match -> hashmap

        // first check = if string sizes not equal, return False impossible to be anagrams
        if (s.size() != t.size()) {
            return false;
        }

        unordered_map<char, int> count_s;
        unordered_map<char, int> count_t;

        for (int i = 0; i < s.size(); i++) {
            // automatic fallback of 0
            count_s[s[i]] += 1;
            count_t[t[i]] += 1;
        }

        if (count_s != count_t) {
            return false;
        }
            
        return true;
    }
};
