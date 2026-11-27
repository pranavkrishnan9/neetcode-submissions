class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #input = int nums[], int k
        #outpuut = k most frequent elements in nums
        bucket = [[] for _ in range(len(nums) + 1)]
        count = {}
        res = []
        for n in nums:
            count[n] = count.get(n, 0) + 1
        for index, freq in count.items():
            bucket[freq].append(index)
        for j in range(len(bucket) - 1, -1, -1):
            for num in bucket[j]:
                if len(res) == k:
                    return res
                res.append(num)
        return res


        