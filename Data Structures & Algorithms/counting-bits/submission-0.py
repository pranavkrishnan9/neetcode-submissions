class Solution:
    def countBits(self, n: int) -> List[int]:
        #input = int n
        #output = # of 1s in every char from [0, n] in array form
        output = []
        for i in range(n+1):
            count = 0
            m=i
            while m > 0:
                count += (m & 1)
                m >>= 1
            output.append(count)
        return output
                
