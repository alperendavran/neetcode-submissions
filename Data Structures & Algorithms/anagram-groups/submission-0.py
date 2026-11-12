class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}

        for word in strs:
            signature = "".join(sorted(word))

            if signature not in groups:
                groups[signature] = []

            groups[signature].append(word)

        return list(groups.values())