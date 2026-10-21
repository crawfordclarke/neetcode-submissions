class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        res = []

        for word in words:
            l, r =  0, len(word) - 1
            while l <= r:
                if word[l] == word[r]:
                    l += 1
                    r -= 1
                else:
                    break
            if l>=r:
                return word       
        return ""
