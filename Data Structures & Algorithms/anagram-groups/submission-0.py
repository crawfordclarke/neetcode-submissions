class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anahash = defaultdict(list)

        for word in strs:

            key = "".join(sorted(word))

            anahash[key].append(word)

        return list(anahash.values())





        