class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        #input = intervals[] where intervals[i] = [start_i, end_i]
        #output = list of all intervals where overlapping intervals are merged
        intervals.sort()
        merged = [intervals[0]]
        for start, end in intervals[1:]:
            if start <= merged[-1][1]:
                if end >= merged[-1][1]:
                    merged[-1][1] = end
            else:
                merged.append([start, end])
        return merged