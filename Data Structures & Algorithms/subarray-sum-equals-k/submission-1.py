class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        pre = defaultdict(int)
        cursum = 0
        res = 0
        pre[0] = 1

        for n in nums:
            cursum += n

            diff = cursum - k

            if diff in pre:
                res += pre[diff]
            pre[cursum] += 1
        return res

        