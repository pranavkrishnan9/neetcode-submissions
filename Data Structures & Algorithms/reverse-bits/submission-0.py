class Solution:
    def reverseBits(self, n: int) -> int:
        #input = int n
        #output = reverse of n in binary
        result = 0
        for _ in range(32):
            result <<= 1
            bit = n & 1
            result |= bit
            n >>= 1
        return result
