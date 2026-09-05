class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []

        def Backtrack(cur, i):
            if i == len(s):
                res.append(cur.copy())
                return 


            for j in range(i, len(s)):
                if self.isPal(s, i, j):
                    cur.append(s[i:j + 1])
                    Backtrack(cur, j + 1)
                    cur.pop()
        Backtrack([], 0)
        return res

    def isPal(self, s, i, j):
        l = i
        r = j
        while l <= r:
            if s[l] != s[r]:
                return False
            l,r = l + 1, r - 1
        return True        

            


