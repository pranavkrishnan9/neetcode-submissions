class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #input = int nums[], int k
        #output = the k most frequent elements within the array
        res = []
        count = {}
        buckets = [[] for _ in range(len(nums) + 1)]
        for n in nums:
            count[n] = count.get(n, 0) + 1
        for num, freq in count.items():
            buckets[freq].append(num)
        for i in range(len(buckets) - 1, 0, -1):
            for n in buckets[i]:
                res.append(n)
                if len(res) == k:
                    return res
        return res
            
        