class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        #input = int temperatures[] where temperatures[i] represents the daily temperature on the ith day
        #output = result[] where result[i] is the number of days after the iths day before a warmer temp appears on a future day

        #all temperatures set to 0 by default
        result = [0] * len(temperatures)
        #create monotonic stack
        stack = []

        for i in range(len(temperatures)):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                days = i - stack[-1]
                result[stack[-1]] = days
                stack.pop()
            stack.append(i)
        return result
