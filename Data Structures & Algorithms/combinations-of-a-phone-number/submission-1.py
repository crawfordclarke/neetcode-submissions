class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        Hashy = {2:"abc", 3:"def", 4:"ghi",
         5:"jkl", 6:"mno", 7:"pqrs", 8:"tuv", 9:"wxyz"}

        def Backtrck(cur, i ):
            if not digits:
                return []

            if i == len(digits):
                res.append("".join(cur))
                return

            for letter in Hashy[int(digits[i])]:
                cur.append(letter)
                Backtrck(cur, i + 1)
                cur.pop()
        Backtrck([],0)     
        return res             


        