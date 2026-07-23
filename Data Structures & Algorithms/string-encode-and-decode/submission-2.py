class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ""
        for s in strs:
            encoded_string += str(len(s)) + '#' + s
        return encoded_string

    def decode(self, s: str) -> List[str]:
        word_len = 0
        i = 0
        decoded_list = []
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            word_len = int(s[i:j])
            start = j + 1
            end = start + word_len
            decoded_list.append(s[start: end])
            i = end
        return decoded_list
