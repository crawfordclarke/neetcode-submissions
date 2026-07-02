class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        res = 0
        Fstack = []
        cars = sorted(zip(position, speed), reverse=True)

        for pos, spd in cars:
            time = (target - pos) / spd

            if not Fstack or time > Fstack[-1]:
                Fstack.append(time)
            
        return len(Fstack)




        