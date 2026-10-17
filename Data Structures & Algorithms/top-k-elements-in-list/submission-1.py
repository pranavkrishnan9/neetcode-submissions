class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #input = int nums[], int k
        #output = the top k frequent elements in nums

        count = {}
        bucket = [[] for i in range(len(nums) + 1)]
        output = []
        for num in nums:
            count[num] = count.get(num, 0) + 1
        for num, freq in count.items():
            bucket[freq].append(num)
        for i in range(len(bucket) - 1, 0, -1):
            for num in bucket[i]:
                output.append(num)
            if len(output) == k:
                return output
            



