class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        l = 0
        for i in range(len(nums)):
            if nums[i] % 2 == 0:
                nums[i], nums[l] = nums[l], nums[i]
                l += 1
        return nums        