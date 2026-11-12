class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}

        for word in strs:
            counts = [0] * 26

            for char in word:
                index = ord(char) - ord("a")
                counts[index] += 1

            signature = tuple(counts)

            if signature not in groups:
                groups[signature] = []

            groups[signature].append(word)

        return list(groups.values())