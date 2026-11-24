class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1

        gas_cost = zip(gas, cost)
        start = 0
        tank = 0

        for i, (g,c) in enumerate(gas_cost):
            tank += g - c

            if tank < 0:
                start = i + 1
                tank = 0
        return start    



            


        