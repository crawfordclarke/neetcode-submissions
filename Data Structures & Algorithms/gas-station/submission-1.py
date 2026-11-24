class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1 

        tank = 0
        start = 0

        for i, (g,c) in enumerate(zip(gas, cost)):
            tank += g - c

            if tank < 0:
                start = i + 1
                tank = 0
        return start      

