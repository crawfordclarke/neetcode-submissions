
class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        if n == 0:
            return 0

        if n == 1:
            return nums[0]
        
        dpf = [0] * n
        dpl = [0] * n

        dpf[0] = 0
        dpf[1] = nums[0]

        dpl[0] = 0
        dpl[1] = nums[1]

        for i in range(2, n):
            dpf[i] = max(dpf[i - 1],
            dpf[i - 2] + nums[i - 1])

            dpl[i] = max(dpl[i - 1],
            dpl[i - 2] + nums[i])

        return max(dpl[n - 1], dpf[n - 1])    

            