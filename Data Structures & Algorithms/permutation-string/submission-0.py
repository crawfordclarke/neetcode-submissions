class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2): return False
        window = len(s1)
        l,r = 0, window
        s1counts = [0] * 26
        windowcounts = [0] * 26


        for c in range(window):
            s1counts[ord(s1[c]) - ord('a')] += 1
            windowcounts[ord(s2[c]) - ord('a')] += 1

        if s1counts == windowcounts: return True


        while r < len(s2):
            windowcounts[ord(s2[l]) - ord('a')] -= 1
            windowcounts[ord(s2[r]) - ord('a')] += 1
            l += 1
            r += 1
            if s1counts == windowcounts: return True
        return False


