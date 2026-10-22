class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        #input1: int[] piles - piles[i] refers to the number of bananas in the ith pile.
        #input2: int h - h refers to the number of hours alloted to eat all the bananas in piles
        #output: int k - k refers to the minimum rate at which you eat bananas that allows you to
        #                eat all the bananas in piles. if a pile has less than k bananas. you can
        #                finish eating the bananas in the pile but are not allowed to move to another

        def hours_req(spd):
            total_time = 0
            for pile in piles:
                total_time += (pile + spd - 1) // spd
            return total_time <= h
        #starting min speed
        left = 1
        #max speed -- binary search from min to max spd
        right = max(piles)
        while left < right:
            mid = left + (right - left) // 2
            if hours_req(mid):
                right = mid
            else:
                left = mid + 1
        #left = right, convergence met
        return left
        
