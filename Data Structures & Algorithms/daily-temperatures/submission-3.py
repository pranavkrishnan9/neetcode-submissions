class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        #input = int temperatures[]
        #output = int res[], where result[i] is the number of days before a warmer temp shows up
        res = [0] * len(temperatures)
        stack = []

        for i in range(len(temperatures)):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                index = stack.pop()
                res[index] = i - index
            stack.append(i)
        return res



