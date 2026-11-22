class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        #input = int intervals[[]] where [] stores a start and end index
        #output = merged overlapping intervals
        intervals.sort()
        merged = [intervals[0]]
        for start, end in intervals[1:]:
            if start <= merged[-1][1]:
                merged[-1][1] = max(merged[-1][1], end)
            else:
                merged.append([start, end])
        return merged

