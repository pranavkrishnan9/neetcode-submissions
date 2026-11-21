class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        #input = intervals [[]] where intervals[i] = [start_i, end_i]
        #output = array of all non overlapping intervals that cover all the intervals in the input
        result = intervals.sort(key=lambda x: x[0])
        merged = [intervals[0]]
        for start, end in intervals[1:]:
            if start <= merged[-1][1]:
                merged[-1][1] = max(merged[-1][1], end)
            else:
                merged.append([start, end])
        return merged