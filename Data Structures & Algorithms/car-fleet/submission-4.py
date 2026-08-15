class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        #input: position[], speed[] where len(position) = n and len(speed) = n, n being the number of cars 
        #traveling to the same destination on a one lane highway
        #position[i] denotes the position of the ith car out of n cars in miles
        #speed[i] denotes the speed of the ith car out of n cars in miles per hour
        #destination is at position target, where target is an integer representing miles

        #car i cannot pass car i+1, however, car i can reach the same position as car i+1 and then drive at the same speed as that car
        #A car fleet is defined as a non empty set of car(s) driving at the same pos and speed
        #If a car catches up to a car fleet the moment the car fleet reaches target, the car is considered to be part of the car fleet

        pairs = sorted(zip(position, speed), reverse=True)
        stack = []
        for position, speed in pairs:
            time = (target-position)/speed
            if not stack or time>stack[-1]:
                stack.append(time)
        return len(stack)


        
        