class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #input = int nums[], int k
        #output = list of the top k frequent elements in nums
        result = []
        output = [[] for i in range(len(nums) + 1)]
        freq = {}

        for i in range(len(nums)):
            #populate frequency hashmap with num frequencies
            freq[nums[i]] = freq.get(nums[i], 0) + 1

        for num, count in freq.items():
            output[count].append(num)

        for j in range(len(output) - 1, 0, -1):
            for num in output[j]:
                result.append(num)
                if len(result) == k:
                    return result
            


        



