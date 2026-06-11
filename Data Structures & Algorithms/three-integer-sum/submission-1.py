class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:


        sort = sorted(nums)

        res = []

    
        for i in range(len(sort)-2):

            if i > 0 and sort[i] == sort[i-1]:
                continue

            target = -sort[i]
            l,r = i + 1, len(sort)-1

            while l < r:
                currentsum = sort[l] + sort[r]
                if currentsum < target:
                    l += 1
                elif currentsum > target:
                    r -= 1
                else:
                    res.append([sort[i], sort[l], sort[r]])
                    l += 1
                    r -= 1
                    while l < r and sort[l] == sort[l - 1]:
                        l += 1
                    while l < r and sort[r] == sort[r + 1]:
                        r -= 1
        return res


                    


        