class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numberset = set(nums)

        maxsequence = 0

        for number in numberset:
            i = 1
            if number - 1 not in numberset:
                sequencecounter = 1
                while number + i in numberset:
                    sequencecounter += 1
                    i += 1
                if sequencecounter > maxsequence:
                    maxsequence = sequencecounter
        return maxsequence
            

        

        