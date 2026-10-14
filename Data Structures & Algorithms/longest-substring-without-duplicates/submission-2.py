class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        r = 0
        seen = set()
        maxlen = 0


        while l <= r and r < len(s):
            if s[r] not in seen:
                seen.add(s[r])
                maxlen = max(maxlen, r - l + 1)
                r += 1
            else:
                seen.remove(s[l])
                l += 1
        return maxlen        

                