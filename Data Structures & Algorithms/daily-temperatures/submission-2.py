class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        #input: tempartures[] -> array of ints
        #temperatures[i] represents the daily temp on the ith day
        #output: result[] -> array of ints
        #result[i] represents the number of days after the ith day before a warmer temp appears on a future day
        #if there is no day in the future where a warmer temp appears for the ith day, result[i] is set to 0
        stack = []
        result = [0] * len(temperatures)
        for i in range(len(temperatures)):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                index = stack.pop()
                result[index] = i - index
            stack.append(i)
        return result


        


        