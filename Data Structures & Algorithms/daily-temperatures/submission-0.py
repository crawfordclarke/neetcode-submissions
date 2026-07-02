class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        indice_stack = []

        print(res)

        for i in range(len(temperatures)):
            current_temp = temperatures[i]


            while indice_stack and current_temp > temperatures[indice_stack[-1]]:

                prev = indice_stack.pop()
                res[prev] = i - prev

            indice_stack.append(i)

        return res



        