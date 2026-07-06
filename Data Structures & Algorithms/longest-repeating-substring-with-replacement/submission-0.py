class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        charDict = defaultdict(int)
        l = 0
        maxFre = 0
        res = 0


        for r in range(len(s)):
            charDict[s[r]] += 1
            maxFre = max(maxFre, max(charDict.values()))
            

            replacements = (r - l + 1) - maxFre

            while replacements > k:
                charDict[s[l]] -= 1
                l += 1
                replacements = (r - l + 1) - maxFre
            res = max(res, (r - l + 1))
                
            
        return res


        