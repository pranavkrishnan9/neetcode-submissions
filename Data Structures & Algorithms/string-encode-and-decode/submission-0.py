class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ""
        delimiter = "#"
        strlen = 0
        for s in strs:
            strlen = str(len(s))
            encoded_string += strlen + delimiter + s
        return encoded_string

    def decode(self, s: str) -> List[str]:
        result = []
        i = 0
        while i < len(s):
            ptr = i
            while s[ptr] != '#':
                ptr += 1
            num = int(s[i:ptr])
            start = ptr+1
            end = start+num
            result.append(s[start:end])
            i = end
        return result
