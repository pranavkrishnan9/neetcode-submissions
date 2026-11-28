class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        #input = array of intervals [start, end],...
        #output = merged array of intervals, where overlapping intervals combine
        intervals.sort()
        merged = [intervals[0]]

        for start, end in intervals[1:]:
            if start <= merged[-1][1]:
                if end >= merged[-1][1]:
                    merged[-1][1] = end
                if start < merged[-1][0]:
                    merged[-1][0] = start
            else:
                merged.append([start, end])

        return merged