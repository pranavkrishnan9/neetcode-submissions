class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        #input = int piles[], int h where piles[i] represents the numbe of bananas in the ith pile and h represents the number of hours you have to eat all the bananas.
        #output = int k, where k is the minimum bananas-per-hour rate at which you can eat all the bananas within h hours. if the pile has <k bananas, you can finish eating the pile but you cannot eat from the same pile within the same hour.
        slowest = 1
        fastest = max(piles)
        spd = fastest
        while slowest <= fastest:
            total_hours = 0
            mid = (fastest + slowest)//2
            for p in piles:
                total_hours += math.ceil(p/mid)
            if total_hours <= h:
                spd = mid
                fastest = mid - 1
            else:
                slowest = mid + 1
        return spd
