class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sub = nums[0]
        sumsofar = 0


        for num in nums:
            sumsofar += num
            max_sub = max(max_sub, sumsofar)
            if sumsofar < 0:
                sumsofar = 0 
        return max_sub        