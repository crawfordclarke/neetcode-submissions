class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        content = 0
        gl = 0
        sl = 0
        g.sort()
        s.sort()
        while gl <= (len(g) - 1) and sl <= (len(s) - 1):
            if s[sl] >= g[gl]:
                content += 1
                gl += 1
                sl += 1
            else:
                sl += 1
        return content        