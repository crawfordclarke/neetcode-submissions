class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l,r = 0, len(heights)-1
        currentmax = 0

        while l < r:
            maxatp = (r-l)*min(heights[l], heights[r])
            if maxatp > currentmax:
                currentmax = maxatp
            if heights[l] < heights[r]:
                 l += 1
            elif heights[l] > heights[r]:
                r -= 1
            elif heights[l] == heights[r]:
                l += 1
                r -= 1
        return currentmax
                





        