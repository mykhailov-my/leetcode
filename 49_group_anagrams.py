# Did with help
class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        word_groups = {}
        for word in strs:
            key = tuple(sorted(word))
            word_groups[key] = word_groups.get(key, []) + [word]
        return word_groups.values()