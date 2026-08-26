class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []



        def Backtrack(cur, opening, close):

            if len(cur) == n * 2:
                res.append("".join(cur))
                return 
            if opening < n:
                cur.append("(")
                Backtrack(cur, opening + 1, close)
                cur.pop()
            if close < opening:
                cur.append(")")
                Backtrack(cur, opening, close + 1)
                cur.pop()
        Backtrack([], 0, 0)       
        return res        






        