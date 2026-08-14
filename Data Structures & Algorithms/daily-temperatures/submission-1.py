class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        #input: tempartures[] -> array of ints
        #temperatures[i] represents the daily temp on the ith day
        #output: result[] -> array of ints
        #result[i] represents the numbers of days after the ith day before a warmer temp appears on a future day
        #if there is no day in the future where a warmer temp appears for the ith day, result[i] is set to 0
        stack = []
        result = [0] * len(temperatures)
        for i in range(len(temperatures)):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                stack_index = stack.pop()
                result[stack_index] = i - stack_index
            stack.append(i)
        return result



        